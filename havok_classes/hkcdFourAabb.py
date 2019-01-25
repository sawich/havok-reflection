from enum import Enum
from .common import vector4
import struct


class BoundIndex(Enum):
    X_MIN = 0
    X_MAX = 1
    Y_MIN = 2
    Y_MAX = 3
    Z_MIN = 4
    Z_MAX = 5


class hkcdFourAabb(object):
    lx: vector4
    hx: vector4
    ly: vector4
    hy: vector4
    lz: vector4
    hz: vector4

    def __init__(self, infile):
        self.lx = struct.unpack('>4f', infile.read(16))
        self.hx = struct.unpack('>4f', infile.read(16))
        self.ly = struct.unpack('>4f', infile.read(16))
        self.hy = struct.unpack('>4f', infile.read(16))
        self.lz = struct.unpack('>4f', infile.read(16))
        self.hz = struct.unpack('>4f', infile.read(16))
