from enum import Enum
import struct


class Type(Enum):
    INVALID = 0
    TRIANGLE = 1
    QUAD = 2
    CUSTOM = 3
    NUM_TYPES = 4


class hkcdStaticMeshTreeBasePrimitive(object):
    indices: int

    def __init__(self, infile):
        self.indices = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} indices={indices}>".format(**{
            "class_name": self.__class__.__name__,
            "indices": self.indices,
        })
