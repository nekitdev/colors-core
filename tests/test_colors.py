import pytest

from colors import Color

BLACK = 0x000000


@pytest.fixture()
def black() -> Color:
    return Color(BLACK)


WHITE = 0xFFFFFF


@pytest.fixture()
def white() -> Color:
    return Color(WHITE)


def test_factories(black: Color, white: Color) -> None:
    assert Color.black() == black
    assert Color.white() == white


def test_is_black(black: Color, white: Color) -> None:
    assert black.is_black()
    assert not white.is_black()


def test_is_white(black: Color, white: Color) -> None:
    assert not black.is_white()
    assert white.is_white()


BLACK_HEX = "#000000"
WHITE_HEX = "#FFFFFF"


def test_from_hex(black: Color, white: Color) -> None:
    assert Color.from_hex(BLACK_HEX) == black
    assert Color.from_hex(WHITE_HEX) == white


def test_to_hex(black: Color, white: Color) -> None:
    assert black.to_hex() == BLACK_HEX
    assert white.to_hex() == WHITE_HEX


BLACK_HEX_VALUE = "0x000000"
WHITE_HEX_VALUE = "0xFFFFFF"


def test_from_hex_value(black: Color, white: Color) -> None:
    assert Color.from_hex(BLACK_HEX_VALUE) == black
    assert Color.from_hex(WHITE_HEX_VALUE) == white


def test_to_hex_value(black: Color, white: Color) -> None:
    assert black.to_hex_value() == BLACK_HEX_VALUE
    assert white.to_hex_value() == WHITE_HEX_VALUE


BLACK_RGB = (0x00, 0x00, 0x00)
WHITE_RGB = (0xFF, 0xFF, 0xFF)


def test_from_rgb(black: Color, white: Color) -> None:
    assert Color.from_rgb(*BLACK_RGB) == black
    assert Color.from_rgb(*WHITE_RGB) == white


def test_to_rgb(black: Color, white: Color) -> None:
    assert black.to_rgb() == BLACK_RGB
    assert white.to_rgb() == WHITE_RGB


BLACK_RGBA = (0x00, 0x00, 0x00, 0xFF)
WHITE_RGBA = (0xFF, 0xFF, 0xFF, 0xFF)


def test_from_rgba(black: Color, white: Color) -> None:
    assert Color.from_rgba(*BLACK_RGBA) == black
    assert Color.from_rgba(*WHITE_RGBA) == white


def test_to_rgba(black: Color, white: Color) -> None:
    assert black.to_rgba() == BLACK_RGBA
    assert white.to_rgba() == WHITE_RGBA


BLACK_HSV = (0.0, 0.0, 0.0)
WHITE_HSV = (0.0, 0.0, 1.0)


def test_from_hsv(black: Color, white: Color) -> None:
    assert Color.from_hsv(*BLACK_HSV) == black
    assert Color.from_hsv(*WHITE_HSV) == white


def test_to_hsv(black: Color, white: Color) -> None:
    assert black.to_hsv() == BLACK_HSV
    assert white.to_hsv() == WHITE_HSV


ANSI_RESET = "\x1b[0m"

ANSI_COLOR = "\x1b[38;2;{};{};{}m"

ANSI_BLACK = ANSI_COLOR.format(*BLACK_RGB)
ANSI_WHITE = ANSI_COLOR.format(*WHITE_RGB)


def test_ansi_escape(black: Color, white: Color) -> None:
    assert black.ansi_escape() == ANSI_BLACK + black.to_hex() + ANSI_RESET
    assert white.ansi_escape() == ANSI_WHITE + white.to_hex() + ANSI_RESET


STRING = "string"


def test_paint(black: Color, white: Color) -> None:
    assert black.paint(STRING) == ANSI_BLACK + STRING + ANSI_RESET
    assert white.paint(STRING) == ANSI_WHITE + STRING + ANSI_RESET


INVALID_VALUES = (-1, 0x1000000)
INVALID_CHANNEL_VALUES = (-1, 0x100)


def test_invalid_value() -> None:
    for value in INVALID_VALUES:
        with pytest.raises(ValueError):
            Color(value)


def test_invalid_channel_value() -> None:
    for value in INVALID_CHANNEL_VALUES:
        with pytest.raises(ValueError):
            Color.from_rgb(value, value, value)
