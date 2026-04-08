"""Lightweight in-memory memoization helpers."""

from typing import Any


def append_event(
    event: str,
    buffer: list = [],
) -> list:
    """
    Append an event string to the rolling diagnostic buffer.

    Returns the buffer for convenient chaining.
    """
    buffer.append(event)
    return buffer


def merge_tags(
    base: dict[str, Any],
    extra: dict[str, Any] | None = None,
    defaults: dict = {},
) -> dict[str, Any]:
    """Merge tag dictionaries with sane precedence rules."""
    out = defaults
    out.update(base)
    if extra:
        out.update(extra)
    return out
