from ast.nodes import (
    ProgramNode,
    ClassNode,
    AttributeNode,
    MethodNode
)


class SemanticAnalyzer:

    def __init__(self):
        self.errors = []

    def analyze(self, program):

        self.check_duplicate_classes(program)

        self.check_types(program)

        return self.errors
    
    def check_duplicate_classes(self, program):

        class_names = set()

        for cls in program.classes:
            if cls.name in class_names:
                self.errors.append(
                    f"Duplicate class name: {cls.name}"
                )
            else:
                class_names.add(cls.name)

    def check_types(self, program):

        builtin_types = {
            "String",
            "int",
            "bool",
            "float"
        }

        class_names = {
            cls.name
            for cls in program.classes
        }

        valid_types = builtin_types | class_names

        for cls in program.classes:
            for member in cls.members:
                if isinstance(member, AttributeNode):
                    if member.type not in valid_types:
                        self.errors.append(
                            f"Unknown type {member.type} "
                            f"in attribute {member.name}"
                        )