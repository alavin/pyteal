import re
from enum import Enum

from .errors import TealTypeError, TealInputError

class TealType(Enum):
    uint64 = 0
    bytes = 1
    anytype = 2
    none = 3

def require_type(actual, expected):
    if actual != expected and (expected == TealType.none or (actual != TealType.anytype and expected != TealType.anytype)):
        raise TealTypeError(actual, expected)

def types_match(type1: TealType, type2: TealType) -> bool:
    if (type1 == TealType.none or type2 == TealType.none) and type1 != type2:
        return False

    if type1 == TealType.anytype or type2 == TealType.anytype:
        return True
    
    return type1 == type2

def valid_address(address:str):
    """ check if address is a valid address with checksum
    """
    if type(address) is not str:
        raise TealInputError("An address needs to be a string")

    if len(address) != 58:
        raise TealInputError("Address length is not correct. Should " +
            "be a base 32 string encoded 32 bytes public key + 4 bytes checksum")

    valid_base32(address)

def valid_base32(s:str):
    """ check if s is a valid base32 encoding string
    """
    pattern = re.compile(r'[A-Z2-9]*') # RFC 4648 base 32 w/o padding

    if pattern.fullmatch(s) is None:
        raise TealInputError("{} is not a valid RFC 4648 base 32 string".format(s))

def valid_base64(s:str):
    """ check if s is a valid base64 encoding string
    """
    pattern = re.compile(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')

    if pattern.fullmatch(s) is None:
        raise TealInputError("{} is not a valid RFC 4648 base 64 string".format(s))

def valid_base16(s:str):
    """ check if s is a valid hex encoding string
    """
    pattern = re.compile(r'[0-9A-Fa-f]*')

    if pattern.fullmatch(s) is None:
        raise TealInputError("{} is not a valid RFC 4648 base 16 string".format(s))

def  valid_tmpl(s:str):
    """ check if s is valid template name
    """
    pattern = re.compile(r'TMPL_[A-Z0-9_]+')

    if pattern.fullmatch(s) is None:
        raise TealInputError("{} is not a valid template variable".format(s))
