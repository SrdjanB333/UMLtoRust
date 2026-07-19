from generated.PlantUMLVisitor import PlantUMLVisitor
from ast.nodes import (
    ProgramNode,
    ClassNode,
    AttributeNode,
    MethodNode,
    ParameterNode

)

class ASTBuilder(PlantUMLVisitor):

    def visitProgram(self, ctx):
        program = ProgramNode()

        for child in ctx.children:
            result = self.visit(child)

            if isinstance(result, ClassNode):
                program.classes.append(result)

        return program
    
    def visitClassDeclaration(self, ctx):
        class_name = ctx.ID().getText()

        class_node = ClassNode(class_name)

        for member_ctx in ctx.member():
            member = self.visit(member_ctx)

            if member is not None:
                class_node.members.append(member)

        return class_node
    
    def visitAttribute(self, ctx):
        visibility = None

        if ctx.visibility():
            visibility = self.visit(ctx.visibility())

        name = ctx.ID().getText()

        type_name = ctx.type_().getText()

        return AttributeNode(
            visibility,
            name,
            type_name
        )
    
    def visitVisibility(self, ctx):
        return ctx.getText()
    
    def visitMethod(self, ctx):
        visibility = None

        if ctx.visibility():
            visibility = self.visit(ctx.visibility())

        name = ctx.ID().getText()

        parameters = []

        if ctx.parametarList():
            parameters = self.visit(ctx.parametarList())

        return_type = None

        if ctx.type_():
            return_type = ctx.type_().getText()

        return MethodNode(
            visibility,
            name,
            parameters,
            return_type
        )
    
    def visitParametarList(self, ctx):
        parameters = []

        for param_ctx in ctx.parametar():
            parameter = self.visit(param_ctx)

            if parameter is not None:
                parameters.append(parameter)

        return parameters
    
    def visitParametar(self, ctx):
        name = ctx.ID().getText()

        type_name = ctx.type_().getText()

        return ParameterNode(
            name,
            type_name
        )