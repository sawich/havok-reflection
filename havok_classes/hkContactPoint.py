import struct


class hkContactPoint(object):
    position: vector4
    separatingNormal: vector4

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.separatingNormal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} position={position}, separatingNormal={separatingNormal}>".format(**{
            "class_name": self.__class__.__name__,
            "position": self.position,
            "separatingNormal": self.separatingNormal,
        })
