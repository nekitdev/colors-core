__all__ = (
    "HEX_BASE",
    "HEX_STRING_PREFIX",
    "HEX_VALUE_PREFIX",
    "hex_string",
    "hex_value",
    "hex_byte_string",
    "hex_byte_value",
)

HEX_BASE = 16

HEX_STRING_PREFIX = "#"
HEX_VALUE_PREFIX = "0x"

HEX_TEMPLATE = "{:0>6X}"
HEX_BYTE = "{:0>2X}"

HEX_STRING = HEX_STRING_PREFIX + HEX_TEMPLATE
HEX_VALUE = HEX_VALUE_PREFIX + HEX_TEMPLATE

HEX_BYTE_STRING = HEX_STRING_PREFIX + HEX_BYTE
HEX_BYTE_VALUE = HEX_VALUE_PREFIX + HEX_BYTE

hex_string = HEX_STRING.format
hex_value = HEX_VALUE.format

hex_byte_string = HEX_BYTE_STRING.format
hex_byte_value = HEX_BYTE_VALUE.format
