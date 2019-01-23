from .hkReferencedObject import hkReferencedObject
from .hkMonitorStreamColorTableColorPair import hkMonitorStreamColorTableColorPair


class hkMonitorStreamColorTable(hkReferencedObject):
	colorPairs: hkMonitorStreamColorTableColorPair
	defaultColor: int
