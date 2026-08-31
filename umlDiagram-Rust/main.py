from antlr4 import *

from grammar.generated.PlantUMLLexer import PlantUMLLexer
from grammar.generated.PlantUMLParser import PlantUMLParser
from semantic.analyzer import SemanticAnalyzer
from generator.rustGenerator import RustGenerator

from ast.visitor import ASTBuilder


def main():

    input_stream = FileStream("C:/Users/PC/Desktop/Srdjan fakultet/III godina/Konstrukcija kompilatora/ProjekatKK/umlDiagram-Rust/examples/zad5.puml")
    lexer = PlantUMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PlantUMLParser(token_stream)
    tree = parser.program()
    builder = ASTBuilder()
    ast = builder.visit(tree)
    analyzer = SemanticAnalyzer()

    errors = analyzer.analyze(ast)


    if errors:
        for error in errors:
            print("ERROR:", error)
        return

    print_ast(ast)

    generator = RustGenerator()

    generator.write_to_files(ast)

    print("Rust kod je uspjesno generisan.")


def print_ast(program):

    for cls in program.classes:
        print("Class:", cls.name)
        for member in cls.members:
            if hasattr(member, "type"):
                print(
                    "Attribute:", member.visibility, member.name, ":", member.type
                )
            else:
                print(
                    "Method:", member.visibility, member.name
                )
                for param in member.parameters:
                    print(
                        "Param:", param.name, ":", param.type
                    )
        print()


if __name__ == "__main__":
    main()