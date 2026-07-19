# Generated from PlantUML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PlantUMLParser import PlantUMLParser
else:
    from PlantUMLParser import PlantUMLParser

# This class defines a complete listener for a parse tree produced by PlantUMLParser.
class PlantUMLListener(ParseTreeListener):

    # Enter a parse tree produced by PlantUMLParser#program.
    def enterProgram(self, ctx:PlantUMLParser.ProgramContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#program.
    def exitProgram(self, ctx:PlantUMLParser.ProgramContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#classDeclaration.
    def enterClassDeclaration(self, ctx:PlantUMLParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#classDeclaration.
    def exitClassDeclaration(self, ctx:PlantUMLParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#member.
    def enterMember(self, ctx:PlantUMLParser.MemberContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#member.
    def exitMember(self, ctx:PlantUMLParser.MemberContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#attribute.
    def enterAttribute(self, ctx:PlantUMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#attribute.
    def exitAttribute(self, ctx:PlantUMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#method.
    def enterMethod(self, ctx:PlantUMLParser.MethodContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#method.
    def exitMethod(self, ctx:PlantUMLParser.MethodContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#visibility.
    def enterVisibility(self, ctx:PlantUMLParser.VisibilityContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#visibility.
    def exitVisibility(self, ctx:PlantUMLParser.VisibilityContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#parametar.
    def enterParametar(self, ctx:PlantUMLParser.ParametarContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#parametar.
    def exitParametar(self, ctx:PlantUMLParser.ParametarContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#parametarList.
    def enterParametarList(self, ctx:PlantUMLParser.ParametarListContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#parametarList.
    def exitParametarList(self, ctx:PlantUMLParser.ParametarListContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#type.
    def enterType(self, ctx:PlantUMLParser.TypeContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#type.
    def exitType(self, ctx:PlantUMLParser.TypeContext):
        pass



del PlantUMLParser