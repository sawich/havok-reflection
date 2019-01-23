from .hclOperator import hclOperator
from .hclSimpleMeshBoneDeformOperatorTriangleBonePair import hclSimpleMeshBoneDeformOperatorTriangleBonePair


class hclSimpleMeshBoneDeformOperator(hclOperator):
	inputBufferIdx: int
	outputTransformSetIdx: int
	triangleBonePairs: hclSimpleMeshBoneDeformOperatorTriangleBonePair
	localBoneTransforms: any
