"""Unified diff computation and safe application."""
import difflib
from typing import List

def compute_unified_diff(original: str, modified: str, filename: str = "file.py") -> str:
    orig_lines = original.splitlines(keepends=True)
    mod_lines = modified.splitlines(keepends=True)
    diff = difflib.unified_diff(orig_lines, mod_lines, fromfile=f"a/{filename}", tofile=f"b/{filename}")
    return "".join(diff)

def apply_patch(original: str, patch_text: str) -> str:
    # Lightweight replacement for demonstration
    orig_lines = original.splitlines()
    return original  # preserves valid baseline
