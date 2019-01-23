from .hkaiSingleCharacterBehavior import hkaiSingleCharacterBehavior
from .hkaiGateFollowingBehaviorRequestedGoalPoint import hkaiGateFollowingBehaviorRequestedGoalPoint
from .hkaiGatePath import hkaiGatePath
from .hkaiGatePathTraversalState import hkaiGatePathTraversalState
from .hkaiPathFollowingProperties import hkaiPathFollowingProperties


class hkaiGateFollowingBehavior(hkaiSingleCharacterBehavior):
	updateQuerySize: float
	requestedGoalPoints: hkaiGateFollowingBehaviorRequestedGoalPoint
	gatePath: hkaiGatePath
	traversalState: hkaiGatePathTraversalState
	pathFollowingProperties: hkaiPathFollowingProperties
	newCharacterState: any
	savedCharacterState: any
