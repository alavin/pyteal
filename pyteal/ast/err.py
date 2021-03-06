from ..types import TealType
from .leafexpr import LeafExpr

class Err(LeafExpr):
    """Expression that causes the program to immediately fail when executed."""

    def __init__(self):
        pass

    def __teal__(self):
        return [["err"]]

    def __str__(self):
        return "(err)"

    def type_of(self):
        return TealType.anytype
