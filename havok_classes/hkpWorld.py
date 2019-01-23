from .hkReferencedObject import hkReferencedObject
from .hkpSimulation import hkpSimulation
from .hkpRigidBody import hkpRigidBody
from .hkMultiThreadCheck import hkMultiThreadCheck
from .hkpPhantom import hkpPhantom


class hkpWorld(hkReferencedObject):
	simulation: hkpSimulation
	gravity: any
	fixedIsland: any
	fixedRigidBody: hkpRigidBody
	activeSimulationIslands: any
	inactiveSimulationIslands: any
	dirtySimulationIslands: any
	maintenanceMgr: any
	memoryWatchDog: any
	assertOnRunningOutOfSolverMemory: bool
	broadPhaseType: any
	broadPhase: any
	broadPhaseDispatcher: any
	phantomBroadPhaseListener: any
	entityEntityBroadPhaseListener: any
	broadPhaseBorderListener: any
	multithreadedSimulationJobData: any
	collisionInput: any
	collisionFilter: any
	collisionDispatcher: any
	convexListFilter: any
	pendingOperations: any
	pendingOperationsCount: int
	pendingBodyOperationsCount: int
	criticalOperationsLockCount: int
	criticalOperationsLockCountForPhantoms: int
	blockExecutingPendingOperations: bool
	criticalOperationsAllowed: bool
	pendingOperationQueues: any
	pendingOperationQueueCount: int
	multiThreadCheck: hkMultiThreadCheck
	processActionsInSingleThread: bool
	allowIntegrationOfIslandsWithoutConstraintsInASeparateJob: bool
	minDesiredIslandSize: int
	modifyConstraintCriticalSection: any
	isLocked: int
	islandDirtyListCriticalSection: any
	propertyMasterLock: any
	wantSimulationIslands: bool
	snapCollisionToConvexEdgeThreshold: float
	snapCollisionToConcaveEdgeThreshold: float
	enableToiWeldRejection: bool
	wantDeactivation: bool
	shouldActivateOnRigidBodyTransformChange: bool
	deactivationReferenceDistance: float
	toiCollisionResponseRotateNormal: float
	maxSectorsPerMidphaseCollideTask: int
	maxSectorsPerNarrowphaseCollideTask: int
	processToisMultithreaded: bool
	maxEntriesPerToiMidphaseCollideTask: int
	maxEntriesPerToiNarrowphaseCollideTask: int
	maxNumToiCollisionPairsSinglethreaded: int
	simulationType: any
	numToisTillAllowedPenetrationSimplifiedToi: float
	numToisTillAllowedPenetrationToi: float
	numToisTillAllowedPenetrationToiHigher: float
	numToisTillAllowedPenetrationToiForced: float
	lastEntityUid: int
	lastIslandUid: int
	lastConstraintUid: int
	phantoms: hkpPhantom
	actionListeners: any
	entityListeners: any
	phantomListeners: any
	constraintListeners: any
	worldDeletionListeners: any
	islandActivationListeners: any
	worldPostSimulationListeners: any
	worldPostIntegrateListeners: any
	worldPostCollideListeners: any
	islandPostIntegrateListeners: any
	islandPostCollideListeners: any
	contactListeners: any
	contactImpulseLimitBreachedListeners: any
	worldExtensions: any
	violatedConstraintArray: any
	broadPhaseBorder: any
	destructionWorld: any
	npWorld: any
	broadPhaseExtents: any
	broadPhaseNumMarkers: int
	sizeOfToiEventQueue: int
	broadPhaseQuerySize: int
	broadPhaseUpdateSize: int
	contactPointGeneration: any
	useCompoundSpuElf: bool
