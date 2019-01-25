from .common import vector4
import struct


class hclBoneSpaceDeformerLocalBlockPNTB(object):
    localPosition: vector4
    localNormal: int
    localTangent: int
    localBiTangent: int

    def __init__(self, infile):
        self.localPosition = struct.unpack('>4f', infile.read(16))
        self.localNormal = struct.unpack('>h', infile.read(2))
        self.localTangent = struct.unpack('>h', infile.read(2))
        self.localBiTangent = struct.unpack('>h', infile.read(2))
