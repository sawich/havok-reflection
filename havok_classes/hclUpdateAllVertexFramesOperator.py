from .hclOperator import hclOperator
from typing import List
from .common import get_array
import struct


class hclUpdateAllVertexFramesOperator(hclOperator):
    vertToNormalID: List[int]
    triangleFlips: List[int]
    referenceVertices: List[int]
    tangentEdgeCosAngle: List[float]
    tangentEdgeSinAngle: List[float]
    biTangentFlip: List[float]
    bufferIdx: int
    numUniqueNormalIDs: int
    updateNormals: bool
    updateTangents: bool
    updateBiTangents: bool

    def __init__(self, infile):
        self.vertToNormalID = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.triangleFlips = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.referenceVertices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.tangentEdgeCosAngle = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.tangentEdgeSinAngle = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.biTangentFlip = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.bufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.numUniqueNormalIDs = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.updateNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.updateTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.updateBiTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertToNormalID=[{vertToNormalID}], triangleFlips=[{triangleFlips}], referenceVertices=[{referenceVertices}], tangentEdgeCosAngle=[{tangentEdgeCosAngle}], tangentEdgeSinAngle=[{tangentEdgeSinAngle}], biTangentFlip=[{biTangentFlip}], bufferIdx={bufferIdx}, numUniqueNormalIDs={numUniqueNormalIDs}, updateNormals={updateNormals}, updateTangents={updateTangents}, updateBiTangents={updateBiTangents}>".format(**{
            "class_name": self.__class__.__name__,
            "vertToNormalID": self.vertToNormalID,
            "triangleFlips": self.triangleFlips,
            "referenceVertices": self.referenceVertices,
            "tangentEdgeCosAngle": self.tangentEdgeCosAngle,
            "tangentEdgeSinAngle": self.tangentEdgeSinAngle,
            "biTangentFlip": self.biTangentFlip,
            "bufferIdx": self.bufferIdx,
            "numUniqueNormalIDs": self.numUniqueNormalIDs,
            "updateNormals": self.updateNormals,
            "updateTangents": self.updateTangents,
            "updateBiTangents": self.updateBiTangents,
        })
