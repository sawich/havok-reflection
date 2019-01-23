from .hkaSkeleton import hkaSkeleton
from .hkaSkeleton import hkaSkeleton
from .hkaSkeletonMapperDataPartitionMappingRange import hkaSkeletonMapperDataPartitionMappingRange
from .hkaSkeletonMapperDataPartitionMappingRange import hkaSkeletonMapperDataPartitionMappingRange
from .hkaSkeletonMapperDataSimpleMapping import hkaSkeletonMapperDataSimpleMapping
from .hkaSkeletonMapperDataChainMapping import hkaSkeletonMapperDataChainMapping


class hkaSkeletonMapperData(object):
	skeletonA: hkaSkeleton
	skeletonB: hkaSkeleton
	partitionMap: any
	simpleMappingPartitionRanges: hkaSkeletonMapperDataPartitionMappingRange
	chainMappingPartitionRanges: hkaSkeletonMapperDataPartitionMappingRange
	simpleMappings: hkaSkeletonMapperDataSimpleMapping
	chainMappings: hkaSkeletonMapperDataChainMapping
	unmappedBones: any
	extractedMotionMapping: any
	keepUnmappedLocal: bool
	mappingType: any