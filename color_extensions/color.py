from __future__ import annotations

from typing import Optional, Type, TypeVar
from colorsys import hsv_to_rgb, rgb_to_hsv

from attrs import Attribute, field, frozen

from color_extensions.ansi import ANSI_COLOR, ANSI_RESET
from color_extensions.constants import (
    BITS, BLACK, BLUE_BYTE, BYTE, DOUBLE_BITS, GREEN_BYTE, RED_BYTE, WHITE, ZERO
)
from color_extensions.hex import (
    HEX_BASE, HEX_STRING_PREFIX, HEX_VALUE_PREFIX, hex_byte_value, hex_string, hex_value
)
from color_extensions.typing import HSV, RGB, RGBA
from color_extensions.utils import byte_to_float, float_to_byte

__all__ = ("Color",)

C = TypeVar("C", bound="Color")

RANGE = "[{}, {}]"

VALUE_RANGE = RANGE.format(hex_value(BLACK), hex_value(WHITE))
CHANNEL_VALUE_RANGE = RANGE.format(hex_byte_value(ZERO), hex_byte_value(BYTE))

EXPECTED_VALUE = f"expected value in {VALUE_RANGE} range"
EXPECTED_CHANNEL_VALUE = f"expected channel value in {CHANNEL_VALUE_RANGE} range"


def validate_value(value: int) -> None:
    if value < BLACK or value > WHITE:
        raise ValueError(EXPECTED_VALUE)


def validate_channel_value(value: int) -> None:
    if value < ZERO or value > BYTE:
        raise ValueError(EXPECTED_CHANNEL_VALUE)


def validate_rgb(red: int, green: int, blue: int) -> None:
    validate_channel_value(red)
    validate_channel_value(green)
    validate_channel_value(blue)


def value_from_rgb(red: int, green: int, blue: int) -> int:
    validate_rgb(red, green, blue)

    return value_from_rgb_unchecked(red, green, blue)


def value_from_rgb_unchecked(red: int, green: int, blue: int) -> int:
    return (red << DOUBLE_BITS) | (green << BITS) | blue


@frozen(order=True)
class Color:
    value: int = field(default=BLACK, repr=hex_value)

    @value.validator
    def validate_value(self, attribute: Attribute[int], value: int) -> None:
        validate_value(value)

    @classmethod
    def black(cls: Type[C]) -> C:
        return cls(BLACK)

    @classmethod
    def white(cls: Type[C]) -> C:
        return cls(WHITE)

    def is_black(self) -> bool:
        return self.value == BLACK

    def is_white(self) -> bool:
        return self.value == WHITE

    def get_byte(self, byte: int) -> int:
        return (self.value >> (BITS * byte)) & BYTE

    @property
    def red(self) -> int:
        return self.get_byte(RED_BYTE)

    @property
    def green(self) -> int:
        return self.get_byte(GREEN_BYTE)

    @property
    def blue(self) -> int:
        return self.get_byte(BLUE_BYTE)

    r = red
    """An alias of [`red`][color_extensions.color.Color.red]."""
    g = green
    """An alias of [`green`][color_extensions.color.Color.green]."""
    b = blue
    """An alias of [`blue`][color_extensions.color.Color.blue]."""

    def ansi_escape(self, string: Optional[str] = None) -> str:
        if string is None:
            string = self.to_hex()

        red, green, blue = self.to_rgb()

        return ANSI_COLOR.format(red, green, blue) + string + ANSI_RESET

    paint = ansi_escape
    """An alias of [`ansi_escape`][color_extensions.color.Color.ansi_escape]."""

    @classmethod
    def from_hex(cls: Type[C], string: str) -> C:
        return cls(int(string.replace(HEX_STRING_PREFIX, HEX_VALUE_PREFIX), HEX_BASE))

    def to_hex(self) -> str:
        return hex_string(self.value)

    def to_hex_value(self) -> str:
        return hex_value(self.value)

    @classmethod
    def from_rgb(cls: Type[C], red: int, green: int, blue: int) -> C:
        return cls(value_from_rgb(red, green, blue))

    def to_rgb(self) -> RGB:
        return (self.red, self.blue, self.green)

    @classmethod
    def from_rgba(cls: Type[C], red: int, green: int, blue: int, alpha: int) -> C:
        return cls.from_rgb(red, green, blue)

    def to_rgba(self, alpha: int = BYTE) -> RGBA:
        return (self.red, self.green, self.blue, alpha)

    @classmethod
    def from_hsv(cls: Type[C], hue: float, saturation: float, value: float) -> C:
        red, green, blue = map(float_to_byte, hsv_to_rgb(hue, saturation, value))

        return cls.from_rgb(red, green, blue)

    def to_hsv(self) -> HSV:
        red, green, blue = map(byte_to_float, self.to_rgb())

        return rgb_to_hsv(red, green, blue)
