from .hkReferencedObject import hkReferencedObject


class hclOperator(hkReferencedObject):
    name: str
    type: enumerate

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.type = enumerate(infile)  # TYPE_ENUM:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} name=\"{name}\", type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "type": self.type,
        })
