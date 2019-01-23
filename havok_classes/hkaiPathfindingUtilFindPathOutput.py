from .hkReferencedObject import hkReferencedObject
from .hkaiPathPathPoint import hkaiPathPathPoint
from .hkaiAstarOutputParameters import hkaiAstarOutputParameters


class hkaiPathfindingUtilFindPathOutput(hkReferencedObject):
	visitedEdges: any
	pathOut: hkaiPathPathPoint
	outputParameters: hkaiAstarOutputParameters
