# Generated from PlantUML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PlantUMLParser import PlantUMLParser
else:
    from PlantUMLParser import PlantUMLParser

# This class defines a complete generic visitor for a parse tree produced by PlantUMLParser.

class PlantUMLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PlantUMLParser#program.
    def visitProgram(self, ctx:PlantUMLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#classDeclaration.
    def visitClassDeclaration(self, ctx:PlantUMLParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#member.
    def visitMember(self, ctx:PlantUMLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#attribute.
    def visitAttribute(self, ctx:PlantUMLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#method.
    def visitMethod(self, ctx:PlantUMLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#visibility.
    def visitVisibility(self, ctx:PlantUMLParser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#parametar.
    def visitParametar(self, ctx:PlantUMLParser.ParametarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#parametarList.
    def visitParametarList(self, ctx:PlantUMLParser.ParametarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#type.
    def visitType(self, ctx:PlantUMLParser.TypeContext):
        return self.visitChildren(ctx)



del PlantUMLParser