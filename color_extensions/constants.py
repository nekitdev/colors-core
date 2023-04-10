__all__ = (
    "ZERO", "BYTE", "BITS", "DOUBLE_BITS", "BLACK", "WHITE", "RED_BYTE", "GREEN_BYTE", "BLUE_BYTE"
)

ZERO = 0x00
BYTE = 0xFF

BITS = BYTE.bit_length()

DOUBLE_BITS = BITS + BITS

BLACK = 0x000000
WHITE = 0xFFFFFF

RED_BYTE = 2
GREEN_BYTE = 1
BLUE_BYTE = 0
