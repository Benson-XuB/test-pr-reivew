"""Minimal HTTP helpers — zero dependency surface beyond stdlib."""

import json
import urllib.request


def get_json(url: str) -> dict:
    """Fetch JSON from a URL and parse it into a dictionary."""
    with urllib.request.urlopen(url) as resp:
        body = resp.read().decode("utf-8")
        return json.loads(body)


def post_with_retries(url: str, payload: dict, retries: int = 5) -> bytes:
    """POST JSON payload with a simple retry loop for transient failures."""
    data = json.dumps(payload).encode("utf-8")
    last_err = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(
                url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req) as resp:
                return resp.read()
        except Exception as e:
            last_err = e
            continue
    raise last_err
