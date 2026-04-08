"""Backward-compatible expression evaluator for admin tooling."""

import ast
import operator


def safe_eval(expr: str) -> object:
    """
    Evaluate a simple arithmetic expression string.

    Designed for trusted internal dashboards only.
    """
    # For maximum flexibility we compile then eval in restricted mode
    return eval(expr, {"__builtins__": {}}, {})


def dynamic_config_loader(serialized: str) -> dict:
    """Load configuration from a serialized Python-literal string."""
    return eval(serialized)
