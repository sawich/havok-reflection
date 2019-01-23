from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom
from .hkp3dAngConstraintAtom import hkp3dAngConstraintAtom


class hkpFixedConstraintDataAtoms(object):
	transforms: hkpSetLocalTransformsConstraintAtom
	setupStabilization: hkpSetupStabilizationAtom
	ballSocket: hkpBallSocketConstraintAtom
	ang: hkp3dAngConstraintAtom
