from .hclVertexSelectionInput import hclVertexSelectionInput
import struct
from .hclVertexFloatInput import hclVertexFloatInput


class hclBonePlanesSetupObjectGlobalPlane(object):
    transformName: str
    particles: hclVertexSelectionInput
    planeEquationBoneSpace: vector4
    allowedPenetration: hclVertexFloatInput
    stiffness: hclVertexFloatInput

    def __init__(self, infile):
        self.transformName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.particles = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.planeEquationBoneSpace = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.allowedPenetration = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transformName=\"{transformName}\", particles={particles}, planeEquationBoneSpace={planeEquationBoneSpace}, allowedPenetration={allowedPenetration}, stiffness={stiffness}>".format(**{
            "class_name": self.__class__.__name__,
            "transformName": self.transformName,
            "particles": self.particles,
            "planeEquationBoneSpace": self.planeEquationBoneSpace,
            "allowedPenetration": self.allowedPenetration,
            "stiffness": self.stiffness,
        })
