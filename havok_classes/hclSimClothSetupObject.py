from .hkReferencedObject import hkReferencedObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclSimClothSetupObjectTransferMotionSetupData import hclSimClothSetupObjectTransferMotionSetupData
from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimClothSetupObjectPerInstanceCollidable import hclSimClothSetupObjectPerInstanceCollidable


class hclSimClothSetupObject(hkReferencedObject):
	name: any
	simulationMesh: hclSimulationSetupMesh
	collidableTransformSet: hclTransformSetSetupObject
	gravity: any
	globalDampingPerSecond: float
	doNormals: bool
	specifyDensity: bool
	vertexDensity: hclVertexFloatInput
	rescaleMass: bool
	totalMass: float
	particleMass: hclVertexFloatInput
	particleRadius: hclVertexFloatInput
	particleFriction: hclVertexFloatInput
	fixedParticles: hclVertexSelectionInput
	enablePinchDetection: bool
	pinchDetectionEnabledParticles: hclVertexSelectionInput
	toAnimPeriod: float
	toSimPeriod: float
	drivePinchedParticlesToReferenceMesh: bool
	pinchReferenceBufferSetup: hclBufferSetupObject
	collisionTolerance: float
	landscapeCollisionParticleSelection: hclVertexSelectionInput
	landscapeCollisionParticleRadius: float
	enableStuckParticleDetection: bool
	stuckParticlesStretchFactor: float
	enableLandscapePinchDetection: bool
	landscapePinchDetectionPriority: int
	landscapePinchDetectionRadius: float
	enableTransferMotion: bool
	transferMotionSetupData: hclSimClothSetupObjectTransferMotionSetupData
	constraintSetSetups: hclConstraintSetSetupObject
	perInstanceCollidables: hclSimClothSetupObjectPerInstanceCollidable
	orderMap: any
