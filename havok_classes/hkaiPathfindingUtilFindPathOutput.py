from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkaiPathPathPoint import hkaiPathPathPoint
from .hkaiAstarOutputParameters import hkaiAstarOutputParameters


class hkaiPathfindingUtilFindPathOutput(hkReferencedObject):
    visitedEdges: any
    pathOut: hkaiPathPathPoint
    outputParameters: hkaiAstarOutputParameters

    def __init__(self, infile):
        self.visitedEdges = any(infile)  # TYPE_ARRAY
        self.pathOut = hkaiPathPathPoint(infile)  # TYPE_ARRAY
        self.outputParameters = hkaiAstarOutputParameters(infile)  # TYPE_STRUCT
