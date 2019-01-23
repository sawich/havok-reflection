from .hkReferencedObject import hkReferencedObject


class hkaFootstepAnalysisInfo(hkReferencedObject):
	name: any
	nameStrike: any
	nameLift: any
	nameLock: any
	nameUnlock: any
	minPos: any
	maxPos: any
	minVel: any
	maxVel: any
	allBonesDown: any
	anyBonesDown: any
	posTol: float
	velTol: float
	duration: float