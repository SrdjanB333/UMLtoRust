# Generated from PlantUML.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,4,0,25,8,0,11,0,12,0,
        26,1,0,1,0,1,0,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,5,2,40,8,2,10,
        2,12,2,43,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,3,4,53,8,4,1,5,3,5,
        56,8,5,1,5,1,5,1,5,1,5,1,6,3,6,63,8,6,1,6,1,6,1,6,3,6,68,8,6,1,6,
        1,6,1,6,3,6,73,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,85,
        8,9,10,9,12,9,88,9,9,3,9,90,8,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,
        10,12,14,16,18,20,0,1,2,0,7,7,9,10,92,0,22,1,0,0,0,2,33,1,0,0,0,
        4,35,1,0,0,0,6,46,1,0,0,0,8,52,1,0,0,0,10,55,1,0,0,0,12,62,1,0,0,
        0,14,74,1,0,0,0,16,76,1,0,0,0,18,89,1,0,0,0,20,91,1,0,0,0,22,24,
        5,2,0,0,23,25,3,2,1,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,
        26,27,1,0,0,0,27,28,1,0,0,0,28,29,5,3,0,0,29,30,5,0,0,1,30,1,1,0,
        0,0,31,34,3,4,2,0,32,34,3,6,3,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,
        1,0,0,0,35,36,5,4,0,0,36,37,5,14,0,0,37,41,5,5,0,0,38,40,3,8,4,0,
        39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,
        0,0,0,43,41,1,0,0,0,44,45,5,6,0,0,45,5,1,0,0,0,46,47,5,14,0,0,47,
        48,5,8,0,0,48,49,5,14,0,0,49,7,1,0,0,0,50,53,3,10,5,0,51,53,3,12,
        6,0,52,50,1,0,0,0,52,51,1,0,0,0,53,9,1,0,0,0,54,56,3,14,7,0,55,54,
        1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,14,0,0,58,59,5,1,0,0,
        59,60,3,20,10,0,60,11,1,0,0,0,61,63,3,14,7,0,62,61,1,0,0,0,62,63,
        1,0,0,0,63,64,1,0,0,0,64,65,5,14,0,0,65,67,5,11,0,0,66,68,3,18,9,
        0,67,66,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,72,5,12,0,0,70,71,
        5,1,0,0,71,73,3,20,10,0,72,70,1,0,0,0,72,73,1,0,0,0,73,13,1,0,0,
        0,74,75,7,0,0,0,75,15,1,0,0,0,76,77,5,14,0,0,77,78,5,1,0,0,78,79,
        3,20,10,0,79,17,1,0,0,0,80,90,3,16,8,0,81,86,3,16,8,0,82,83,5,13,
        0,0,83,85,3,16,8,0,84,82,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,
        87,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,89,80,1,0,0,0,89,81,1,0,0,
        0,90,19,1,0,0,0,91,92,5,14,0,0,92,21,1,0,0,0,10,26,33,41,52,55,62,
        67,72,86,89
    ]

class PlantUMLParser ( Parser ):

    grammarFileName = "PlantUML.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'@startuml'", "'@enduml'", "'class'", 
                     "'{'", "'}'", "'+'", "<INVALID>", "'-'", "'#'", "'('", 
                     "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "STARTUML", "ENDUML", "CLASS", 
                      "LBRACE", "RBRACE", "PLUS", "RELATION", "MINUS", "HASH", 
                      "LPAREN", "RPAREN", "COMMA", "ID", "WS" ]

    RULE_program = 0
    RULE_element = 1
    RULE_classDeclaration = 2
    RULE_relation = 3
    RULE_member = 4
    RULE_attribute = 5
    RULE_method = 6
    RULE_visibility = 7
    RULE_parametar = 8
    RULE_parametarList = 9
    RULE_type = 10

    ruleNames =  [ "program", "element", "classDeclaration", "relation", 
                   "member", "attribute", "method", "visibility", "parametar", 
                   "parametarList", "type" ]

    EOF = Token.EOF
    T__0=1
    STARTUML=2
    ENDUML=3
    CLASS=4
    LBRACE=5
    RBRACE=6
    PLUS=7
    RELATION=8
    MINUS=9
    HASH=10
    LPAREN=11
    RPAREN=12
    COMMA=13
    ID=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STARTUML(self):
            return self.getToken(PlantUMLParser.STARTUML, 0)

        def ENDUML(self):
            return self.getToken(PlantUMLParser.ENDUML, 0)

        def EOF(self):
            return self.getToken(PlantUMLParser.EOF, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PlantUMLParser.ElementContext)
            else:
                return self.getTypedRuleContext(PlantUMLParser.ElementContext,i)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PlantUMLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(PlantUMLParser.STARTUML)
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.element()
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4 or _la==14):
                    break

            self.state = 28
            self.match(PlantUMLParser.ENDUML)
            self.state = 29
            self.match(PlantUMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(PlantUMLParser.ClassDeclarationContext,0)


        def relation(self):
            return self.getTypedRuleContext(PlantUMLParser.RelationContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = PlantUMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.classDeclaration()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.relation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(PlantUMLParser.CLASS, 0)

        def ID(self):
            return self.getToken(PlantUMLParser.ID, 0)

        def LBRACE(self):
            return self.getToken(PlantUMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PlantUMLParser.RBRACE, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PlantUMLParser.MemberContext)
            else:
                return self.getTypedRuleContext(PlantUMLParser.MemberContext,i)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = PlantUMLParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(PlantUMLParser.CLASS)
            self.state = 36
            self.match(PlantUMLParser.ID)
            self.state = 37
            self.match(PlantUMLParser.LBRACE)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18048) != 0):
                self.state = 38
                self.member()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(PlantUMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.ID)
            else:
                return self.getToken(PlantUMLParser.ID, i)

        def RELATION(self):
            return self.getToken(PlantUMLParser.RELATION, 0)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = PlantUMLParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(PlantUMLParser.ID)
            self.state = 47
            self.match(PlantUMLParser.RELATION)
            self.state = 48
            self.match(PlantUMLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(PlantUMLParser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(PlantUMLParser.MethodContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember" ):
                listener.enterMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember" ):
                listener.exitMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = PlantUMLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PlantUMLParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(PlantUMLParser.TypeContext,0)


        def visibility(self):
            return self.getTypedRuleContext(PlantUMLParser.VisibilityContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = PlantUMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1664) != 0):
                self.state = 54
                self.visibility()


            self.state = 57
            self.match(PlantUMLParser.ID)
            self.state = 58
            self.match(PlantUMLParser.T__0)
            self.state = 59
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PlantUMLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PlantUMLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PlantUMLParser.RPAREN, 0)

        def visibility(self):
            return self.getTypedRuleContext(PlantUMLParser.VisibilityContext,0)


        def parametarList(self):
            return self.getTypedRuleContext(PlantUMLParser.ParametarListContext,0)


        def type_(self):
            return self.getTypedRuleContext(PlantUMLParser.TypeContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = PlantUMLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1664) != 0):
                self.state = 61
                self.visibility()


            self.state = 64
            self.match(PlantUMLParser.ID)
            self.state = 65
            self.match(PlantUMLParser.LPAREN)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 66
                self.parametarList()


            self.state = 69
            self.match(PlantUMLParser.RPAREN)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 70
                self.match(PlantUMLParser.T__0)
                self.state = 71
                self.type_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisibilityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(PlantUMLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PlantUMLParser.MINUS, 0)

        def HASH(self):
            return self.getToken(PlantUMLParser.HASH, 0)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_visibility

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisibility" ):
                listener.enterVisibility(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisibility" ):
                listener.exitVisibility(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisibility" ):
                return visitor.visitVisibility(self)
            else:
                return visitor.visitChildren(self)




    def visibility(self):

        localctx = PlantUMLParser.VisibilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_visibility)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1664) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PlantUMLParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(PlantUMLParser.TypeContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_parametar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametar" ):
                listener.enterParametar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametar" ):
                listener.exitParametar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametar" ):
                return visitor.visitParametar(self)
            else:
                return visitor.visitChildren(self)




    def parametar(self):

        localctx = PlantUMLParser.ParametarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(PlantUMLParser.ID)
            self.state = 77
            self.match(PlantUMLParser.T__0)
            self.state = 78
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametarListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PlantUMLParser.ParametarContext)
            else:
                return self.getTypedRuleContext(PlantUMLParser.ParametarContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.COMMA)
            else:
                return self.getToken(PlantUMLParser.COMMA, i)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_parametarList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametarList" ):
                listener.enterParametarList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametarList" ):
                listener.exitParametarList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametarList" ):
                return visitor.visitParametarList(self)
            else:
                return visitor.visitChildren(self)




    def parametarList(self):

        localctx = PlantUMLParser.ParametarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parametarList)
        self._la = 0 # Token type
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.parametar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.parametar()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 82
                    self.match(PlantUMLParser.COMMA)
                    self.state = 83
                    self.parametar()
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PlantUMLParser.ID, 0)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PlantUMLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(PlantUMLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





