__all__ = (
    "ZERO",
    "BYTE",
    "BITS",
    "DOUBLE_BITS",
    "BLACK",
    "WHITE",
    "RED_BYTE",
    "GREEN_BYTE",
    "BLUE_BYTE",
)

ZERO = 0x00
"""The zero byte value."""
BYTE = 0xFF
"""The full byte value."""

BITS = BYTE.bit_length()
"""The amount of bits in one byte."""

DOUBLE_BITS = BITS + BITS
"""The amount of bits in two bytes."""

BLACK = 0x000000
"""The black color value."""
WHITE = 0xFFFFFF
"""The white color value."""

RED_BYTE = 2
"""The byte representing the red channel."""
GREEN_BYTE = 1
"""The byte representing the green channel."""
BLUE_BYTE = 0
"""The byte representing the blue channel."""
