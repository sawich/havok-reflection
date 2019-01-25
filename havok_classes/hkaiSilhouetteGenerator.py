from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .enums import GeneratorType
from .hkaiConvexSilhouetteSet import hkaiConvexSilhouetteSet
from .hkQTransform import hkQTransform


class GeneratorType(Enum):
    GENERATOR_PHYSICS_2012_BODY = 0
    GENERATOR_POINT_CLOUD = 1
    GENERATOR_STORAGE_POINT_CLOUD_REMOVED = 2
    GENERATOR_PHYSICS_BODY_BASE = 3
    GENERATOR_PHYSICS_BODY = 4
    GENERATOR_USER_0 = 5
    GENERATOR_USER_1 = 6
    GENERATOR_USER_2 = 7
    GENERATOR_USER_3 = 8
    GENERATOR_MAX = 9


class ForceGenerateOntoPpuReasons(Enum):
    FORCE_PPU_USER_REQUEST = 8
    FORCE_PPU_SILHOUETTE_COMPLEXITY_REQUEST = 16


class ExpansionFlags(Enum):
    AABB_EXPAND_NONE = 0
    AABB_EXTRUDE_DOWN = 1
    AABB_EXPAND_PLANAR = 2
    AABB_EXPAND_UNIFORM = 4


class hkaiSilhouetteGenerator(hkReferencedObject):
    userData: int
    lazyRecomputeDisplacementThreshold: float
    type: GeneratorType
    forceGenerateOntoPpu: int
    materialId: int
    cachedSilhouettes: hkaiConvexSilhouetteSet
    transform: hkQTransform

    def __init__(self, infile):
        self.userData = struct.unpack('>L', infile.read(8))
        self.lazyRecomputeDisplacementThreshold = struct.unpack('>f', infile.read(4))
        self.type = GeneratorType(infile)  # TYPE_ENUM
        self.forceGenerateOntoPpu = struct.unpack('>B', infile.read(1))
        self.materialId = struct.unpack('>i', infile.read(4))
        self.cachedSilhouettes = hkaiConvexSilhouetteSet(infile)  # TYPE_POINTER
        self.transform = hkQTransform(infile)  # TYPE_STRUCT
