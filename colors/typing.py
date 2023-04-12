from typing import Tuple

__all__ = ("RGB", "RGBA", "HSV")

RGB = Tuple[int, int, int]
"""Represents *RGB* color tuples."""
RGBA = Tuple[int, int, int, int]
"""Represents *RGBA* color tuples."""
HSV = Tuple[float, float, float]
"""Represents *HSV* color tuples."""
