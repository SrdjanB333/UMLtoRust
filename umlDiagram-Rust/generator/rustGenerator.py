from ast.nodes import (
    ProgramNode,
    ClassNode,
    AttributeNode,
    MethodNode
)


class RustGenerator:

    def __init__(self):
        self.output = []

    def generate(self, program):

        for cls in program.classes:
            self.generate_class(cls)

        return "\n".join(self.output)
    
    def generate_class(self, cls):

        self.output.append(f"pub struct {cls.name} {{")
        for member in cls.members:
            if isinstance(member, AttributeNode):
                self.generate_attribute(member)

        self.output.append("}")
        self.output.append("")

    def generate_attribute(self, attribute):

        rust_type = self.map_type(attribute.type)

        self.output.append(f"{attribute.name}: {rust_type},")

    def map_type(self, uml_type):

        mapping = {
            "String": "String",
            "int": "i32",
            "bool": "bool",
            "float": "f64"
        }

        return mapping.get(
            uml_type,
            uml_type
        )