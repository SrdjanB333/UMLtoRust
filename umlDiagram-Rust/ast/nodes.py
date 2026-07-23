class ProgramNode:
    def __init__(self):
        self.classes = []
        self.relations = []

class ClassNode:
    def __init__(self, name):
        self.name = name
        self.members = []

class AttributeNode:
    def __init__(self, visibility, name, type_name):
        self.visibility = visibility
        self.name = name
        self.type = type_name

class MethodNode:
    def __init__(self, visibility, name, parameters, return_type):
        self.visibility = visibility
        self.name = name
        self.parameters = parameters
        self.return_type = return_type

class ParameterNode:
    def __init__(self, name, type_name):
        self.name = name
        self.type = type_name

class RelationNode:

    def __init__(self, source, relation_type, target):

        self.source = source
        self.relation_type = relation_type
        self.target = target