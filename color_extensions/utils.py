from color_extensions.constants import BYTE

__all__ = ("float_to_byte", "byte_to_float")


def float_to_byte(value: float) -> int:
    return int(value * BYTE)


def byte_to_float(value: int) -> float:
    return value / BYTE
