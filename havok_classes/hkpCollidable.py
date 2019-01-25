from .hkpCdBody import hkpCdBody
from enum import Enum
import struct
from .hkpTypedBroadPhaseHandle import hkpTypedBroadPhaseHandle
from .hkpCollidableBoundingVolumeData import hkpCollidableBoundingVolumeData


class ForceCollideOntoPpuReasons(Enum):
    FORCE_PPU_USER_REQUEST = 1
    FORCE_PPU_SHAPE_REQUEST = 2
    FORCE_PPU_MODIFIER_REQUEST = 4
    FORCE_PPU_SHAPE_UNCHECKED = 8


class hkpCollidable(hkpCdBody):
    ownerOffset: int
    forceCollideOntoPpu: int
    shapeSizeOnSpu: int
    broadPhaseHandle: hkpTypedBroadPhaseHandle
    boundingVolumeData: hkpCollidableBoundingVolumeData
    allowedPenetrationDepth: float

    def __init__(self, infile):
        self.ownerOffset = struct.unpack('>b', infile.read(1))
        self.forceCollideOntoPpu = struct.unpack('>B', infile.read(1))
        self.shapeSizeOnSpu = struct.unpack('>H', infile.read(2))
        self.broadPhaseHandle = hkpTypedBroadPhaseHandle(infile)  # TYPE_STRUCT
        self.boundingVolumeData = hkpCollidableBoundingVolumeData(infile)  # TYPE_STRUCT
        self.allowedPenetrationDepth = struct.unpack('>f', infile.read(4))
