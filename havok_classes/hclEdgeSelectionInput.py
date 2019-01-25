from enum import Enum
from .enums import EdgeSelectionType


class EdgeSelectionType(Enum):
    EDGE_SELECTION_ALL = 0
    EDGE_SELECTION_NONE = 1
    EDGE_SELECTION_CHANNEL = 2
    EDGE_SELECTION_INVERSE_CHANNEL = 3


class hclEdgeSelectionInput(object):
    type: EdgeSelectionType
    channelName: str

    def __init__(self, infile):
        self.type = EdgeSelectionType(infile)  # TYPE_ENUM
        self.channelName = struct.unpack('>s', infile.read(0))
