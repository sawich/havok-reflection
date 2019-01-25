import struct


class hclCompressibleLinkConstraintSetLink(object):
    particleA: int
    particleB: int
    restLength: float
    compressionLength: float
    stiffness: float

    def __init__(self, infile):
        self.particleA = struct.unpack('>H', infile.read(2))
        self.particleB = struct.unpack('>H', infile.read(2))
        self.restLength = struct.unpack('>f', infile.read(4))
        self.compressionLength = struct.unpack('>f', infile.read(4))
        self.stiffness = struct.unpack('>f', infile.read(4))
