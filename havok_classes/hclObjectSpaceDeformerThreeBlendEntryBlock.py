import struct


class hclObjectSpaceDeformerThreeBlendEntryBlock(object):
    vertexIndices: int
    boneIndices: int
    boneWeights: int

    def __init__(self, infile):
        self.vertexIndices = struct.unpack('>H', infile.read(2))
        self.boneIndices = struct.unpack('>H', infile.read(2))
        self.boneWeights = struct.unpack('>B', infile.read(1))
