from .hkaiBehavior import hkaiBehavior
from .hkaiCharacter import hkaiCharacter
from .hkaiNavMeshPathRequestInfo import hkaiNavMeshPathRequestInfo
from .hkaiNavVolumePathRequestInfo import hkaiNavVolumePathRequestInfo
from .hkaiSingleCharacterBehaviorRequestedGoalPoint import hkaiSingleCharacterBehaviorRequestedGoalPoint


class hkaiSingleCharacterBehavior(hkaiBehavior):
	character: hkaiCharacter
	callbackType: any
	immediateNavMeshRequest: hkaiNavMeshPathRequestInfo
	immediateNavVolumeRequest: hkaiNavVolumePathRequestInfo
	requestedGoalPoints: hkaiSingleCharacterBehaviorRequestedGoalPoint
	currentGoalIndex: int