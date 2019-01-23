from .hkReferencedObject import hkReferencedObject
from .hkaiAvoidanceSolverSphereObstacle import hkaiAvoidanceSolverSphereObstacle
from .hkaiAvoidanceSolverBoundaryObstacle import hkaiAvoidanceSolverBoundaryObstacle


class hkaiObstacleGenerator(hkReferencedObject):
	useSpheres: bool
	useBoundaries: bool
	clipBoundaries: bool
	transform: any
	spheres: hkaiAvoidanceSolverSphereObstacle
	boundaries: hkaiAvoidanceSolverBoundaryObstacle
	userData: int
