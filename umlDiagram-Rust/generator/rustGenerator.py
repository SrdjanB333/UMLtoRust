from ast.nodes import (
    ProgramNode,
    ClassNode,
    AttributeNode,
    MethodNode,
    RelationNode
)
import os


class RustGenerator:

    def __init__(self):
        self.output = []

    def generate(self, program):

        self.program = program

        for cls in program.classes:
            self.generate_class(cls)

        return "\n".join(self.output)
    
    def generate_class(self, cls):

        # Generisanje struct-a
        self.output.append(f"pub struct {cls.name} {{")

        for member in cls.members:
            if isinstance(member, AttributeNode):
                self.generate_attribute(member)

        # Dodavanje relacija
        for relation in self.program.relations:
            self.generate_relation(
                relation,
                cls
            )

        self.output.append("}")
        self.output.append("")

        # Izdvajanje metoda
        methods = []

        for member in cls.members:
            if isinstance(member, MethodNode):
                methods.append(member)

        # Generisanje impl bloka
        if methods:
            self.output.append(f"impl {cls.name} {{")
            for method in methods:
                self.generate_method(method)

            self.output.append("}")
            self.output.append("")

    def generate_attribute(self, attribute):

        rust_type = self.map_type(attribute.type)

        self.output.append(
            f"    {attribute.name}: {rust_type},"
            )
    
    def generate_method(self, method):

        visibility = self.map_visibility(method.visibility)
        parameters = self.generate_parameters(method.parameters)
        return_type = ""

        if method.return_type:
            return_type = f" -> {self.map_type(method.return_type)}"

        self.output.append(
            f"    {visibility}fn {method.name}({parameters}){return_type} {{"
        )

        self.output.append("        // TODO: implement")

        self.output.append("    }")
        self.output.append("")

    def generate_parameters(self, parameters):

        result = ["&self"]

        for parameter in parameters:
            result.append(
                f"   {parameter.name}: {self.map_type(parameter.type)}"
            )

        return ", ".join(result)
    
    def generate_relation(self, relation, cls):

        if relation.source != cls.name:
            return

        field_name = relation.target.lower()

        if relation.relation_type == "-->":
            self.output.append(
                f"    {field_name}: {relation.target},"
            )

        elif relation.relation_type == "o--":
            self.output.append(
                f"    {field_name}: {relation.target},"
            )

        elif relation.relation_type == "*--":
            self.output.append(
                f"    {field_name}: Box<{relation.target}>,"
            )
    
    def map_visibility(self, visibility):

        if visibility == "+":
            return "pub "

        return ""
    
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
    
    def generate_inheritance(self, relation):

        parent = relation.source
        child = relation.target

        self.output.append(
            f"pub trait {parent} {{"
        )
        self.output.append(
            "}"
        )
        self.output.append("")
        self.output.append(
            f"impl {parent} for {child} {{"
        )
        self.output.append(
            "}"
        )
        self.output.append("")
    








    def write_to_files(self, program):

        self.program = program

        for cls in program.classes:
            self.output = []
            self.generate_class(cls)
            filename = os.path.join(
                "umlDiagram-Rust",
                "output",
                f"{cls.name}.rs"
            )

            with open(filename, "w", encoding="utf-8") as file:
                file.write("\n".join(self.output))
        
        for relation in program.relations:
            if relation.relation_type == "<|--":
                self.generate_inheritance(
                    relation
                )