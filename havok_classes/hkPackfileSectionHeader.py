

class hkPackfileSectionHeader(object):
	sectionTag: str
	nullByte: str
	absoluteDataStart: int
	localFixupsOffset: int
	globalFixupsOffset: int
	virtualFixupsOffset: int
	exportsOffset: int
	importsOffset: int
	endOffset: int
	pad: int
