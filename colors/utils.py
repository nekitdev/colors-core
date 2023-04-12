from colors.constants import BYTE

__all__ = ("float_to_byte", "byte_to_float")


def float_to_byte(value: float) -> int:
    """Converts the float `value` in range `[0, 1]` to the corresponding byte value in range `[0, 255]`.

    Arguments:
        value: The value to convert.

    Returns:
        The converted value.
    """
    return int(value * BYTE)


def byte_to_float(value: int) -> float:
    """Converts the byte `value` in range `[0, 255]` to the corresponding float value in range `[0, 1]`.

    Arguments:
        value: The value to convert.

    Returns:
        The converted value.
    """
    return value / BYTE
