from .hclConstraintSet import hclConstraintSet
from .hclVolumeConstraintMxFrameBatchData import hclVolumeConstraintMxFrameBatchData
from .hclVolumeConstraintMxFrameSingleData import hclVolumeConstraintMxFrameSingleData
from .hclVolumeConstraintMxApplyBatchData import hclVolumeConstraintMxApplyBatchData
from .hclVolumeConstraintMxApplySingleData import hclVolumeConstraintMxApplySingleData


class hclVolumeConstraintMx(hclConstraintSet):
	frameBatchDatas: hclVolumeConstraintMxFrameBatchData
	frameSingleDatas: hclVolumeConstraintMxFrameSingleData
	applyBatchDatas: hclVolumeConstraintMxApplyBatchData
	applySingleDatas: hclVolumeConstraintMxApplySingleData