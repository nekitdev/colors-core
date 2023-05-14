from __future__ import annotations

from colorsys import hsv_to_rgb, rgb_to_hsv
from typing import Optional, Type, TypeVar

from attrs import Attribute, field, frozen

from colors.ansi import ANSI_COLOR, ANSI_RESET
from colors.constants import (
    BITS,
    BLACK,
    BLUE_BYTE,
    BYTE,
    DOUBLE_BITS,
    GREEN_BYTE,
    RED_BYTE,
    WHITE,
    ZERO,
)
from colors.hex import (
    HEX_BASE,
    HEX_STRING_PREFIX,
    HEX_VALUE_PREFIX,
    hex_byte_value,
    hex_string,
    hex_value,
)
from colors.typing import HSV, RGB, RGBA
from colors.utils import byte_to_float, float_to_byte

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
    """The color value in range from [`BLACK`][colors.constants.BLACK]
    to [`WHITE`][colors.constants.WHITE] (both inclusive).
    """

    @value.validator
    def validate_value(self, attribute: Attribute[int], value: int) -> None:
        validate_value(value)

    @classmethod
    def black(cls: Type[C]) -> C:
        """Creates a color with the [`BLACK`][colors.constants.BLACK] value.

        Returns:
            The color with the black value.
        """
        return cls(BLACK)

    @classmethod
    def white(cls: Type[C]) -> C:
        """Creates a color with the [`WHITE`][colors.constants.WHITE] value.

        Returns:
            The color with the white value.
        """
        return cls(WHITE)

    def is_black(self) -> bool:
        """Checks if the color has the [`BLACK`][colors.constants.BLACK] value.

        Returns:
            Whether the color has the black value.
        """
        return self.value == BLACK

    def is_white(self) -> bool:
        """Checks if the color has the [`WHITE`][colors.constants.WHITE] value.

        Returns:
            Whether the color has the white value.
        """
        return self.value == WHITE

    def get_byte(self, byte: int) -> int:
        """Fetches the byte from the color value.

        Arguments:
            byte: The byte index.

        Returns:
            The byte value.
        """
        return (self.value >> (BITS * byte)) & BYTE

    @property
    def red(self) -> int:
        """The red channel value."""
        return self.get_byte(RED_BYTE)

    @property
    def green(self) -> int:
        """The green channel value."""
        return self.get_byte(GREEN_BYTE)

    @property
    def blue(self) -> int:
        """The blue channel value."""
        return self.get_byte(BLUE_BYTE)

    r = red
    """An alias of [`red`][colors.core.Color.red]."""
    g = green
    """An alias of [`green`][colors.core.Color.green]."""
    b = blue
    """An alias of [`blue`][colors.core.Color.blue]."""

    def ansi_escape(self, string: Optional[str] = None) -> str:
        """Paints the `string` with the color using ANSI escape sequences.

        If the `string` is not given, [`color.to_hex()`][colors.core.Color.to_hex] will be used.

        Arguments:
            string: The string to paint.

        Returns:
            The painted string.
        """
        if string is None:
            string = self.to_hex()

        red, green, blue = self.to_rgb()

        return ANSI_COLOR.format(red, green, blue) + string + ANSI_RESET

    paint = ansi_escape
    """An alias of [`ansi_escape`][colors.core.Color.ansi_escape]."""

    @classmethod
    def from_hex(cls: Type[C], string: str) -> C:
        """Creates a color from the hex `string` (e.g. `#000000`, `0x000000`, or simply `000000`).

        This method uses the [`int`][int] function with the hex base to parse the string,
        replacing `#` with `0x`.

        Arguments:
            string: The hex string.

        Returns:
            The color with the parsed hex value.
        """
        return cls(int(string.replace(HEX_STRING_PREFIX, HEX_VALUE_PREFIX), HEX_BASE))

    def to_hex(self) -> str:
        """Converts the color to the hex string (e.g. `#FFFFFF`).

        Returns:
            The color hex string.
        """
        return hex_string(self.value)

    def to_hex_value(self) -> str:
        """Converts the color to the hex *value* string (e.g. `0xFFFFFF`).

        Returns:
            The color hex *value* string.
        """
        return hex_value(self.value)

    @classmethod
    def from_rgb(cls: Type[C], red: int, green: int, blue: int) -> C:
        """Creates a color from *RGB* values (each in `[0, 255]` range).

        Arguments:
            red: The red channel value.
            green: The green channel value.
            blue: The blue channel value.

        Returns:
            The color created from *RGB* values.
        """
        return cls(value_from_rgb(red, green, blue))

    def to_rgb(self) -> RGB:
        """Converts the color to *RGB* values (each in `[0, 255]` range).

        Returns:
            The *RGB* values.
        """
        return (self.red, self.green, self.blue)

    @classmethod
    def from_rgba(cls: Type[C], red: int, green: int, blue: int, alpha: int) -> C:
        """Creates a color from *RGBA* values (each in `[0, 255]` range).

        Note:
            The *alpha* channel is simply ignored.

        Arguments:
            red: The red channel value.
            green: The green channel value.
            blue: The blue channel value.
            alpha: The alpha channel value.

        Returns:
            The color created from *RGBA* channel values.
        """
        return cls.from_rgb(red, green, blue)

    def to_rgba(self, alpha: int = BYTE) -> RGBA:
        """Converts the color to *RGBA* channel values (each in `[0, 255]` range).

        Arguments:
            alpha: The alpha channel value.

        Returns:
            The *RGBA* values.
        """
        return (self.red, self.green, self.blue, alpha)

    @classmethod
    def from_hsv(cls: Type[C], hue: float, saturation: float, value: float) -> C:
        """Creates a color from *HSV* values (each in `[0, 1]` range).

        Arguments:
            hue: The hue of the color.
            saturation: The saturation of the color.
            value: The value of the color.

        Returns:
            The color created from *HSV* values.
        """
        red, green, blue = map(float_to_byte, hsv_to_rgb(hue, saturation, value))

        return cls.from_rgb(red, green, blue)

    def to_hsv(self) -> HSV:
        """Converts the color to *HSV* values (each in `[0, 1]` range).

        Returns:
            The *HSV* values.
        """
        red, green, blue = map(byte_to_float, self.to_rgb())

        return rgb_to_hsv(red, green, blue)
