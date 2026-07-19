from antlr4 import *

from generated.PlantUMLLexer import PlantUMLLexer
from generated.PlantUMLParser import PlantUMLParser
from semantic.analyzer import SemanticAnalyzer

from ast.visitor import ASTBuilder


def main():

    input_stream = FileStream("C:/Users/PC/Desktop/Srdjan fakultet/III godina/Konstrukcija kompilatora/ProjekatKK/umlDiagram-Rust/examples/zad1.puml")
    lexer = PlantUMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PlantUMLParser(token_stream)
    tree = parser.program()
    builder = ASTBuilder()
    ast = builder.visit(tree)
    analyzer = SemanticAnalyzer()

    errors = analyzer.analyze(ast)


    for error in errors:
        print("ERROR:", error)

    print_ast(ast)


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