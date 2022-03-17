# Generated from ./parser/cypher/Cypher.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CypherParser import CypherParser
else:
    from CypherParser import CypherParser

# This class defines a complete listener for a parse tree produced by CypherParser.
class CypherListener(ParseTreeListener):

    # Enter a parse tree produced by CypherParser#root.
    def enterRoot(self, ctx:CypherParser.RootContext):
        pass

    # Exit a parse tree produced by CypherParser#root.
    def exitRoot(self, ctx:CypherParser.RootContext):
        pass


    # Enter a parse tree produced by CypherParser#query.
    def enterQuery(self, ctx:CypherParser.QueryContext):
        pass

    # Exit a parse tree produced by CypherParser#query.
    def exitQuery(self, ctx:CypherParser.QueryContext):
        pass


    # Enter a parse tree produced by CypherParser#forwardTriple.
    def enterForwardTriple(self, ctx:CypherParser.ForwardTripleContext):
        pass

    # Exit a parse tree produced by CypherParser#forwardTriple.
    def exitForwardTriple(self, ctx:CypherParser.ForwardTripleContext):
        pass


    # Enter a parse tree produced by CypherParser#backwardTriple.
    def enterBackwardTriple(self, ctx:CypherParser.BackwardTripleContext):
        pass

    # Exit a parse tree produced by CypherParser#backwardTriple.
    def exitBackwardTriple(self, ctx:CypherParser.BackwardTripleContext):
        pass


    # Enter a parse tree produced by CypherParser#nodeTriple.
    def enterNodeTriple(self, ctx:CypherParser.NodeTripleContext):
        pass

    # Exit a parse tree produced by CypherParser#nodeTriple.
    def exitNodeTriple(self, ctx:CypherParser.NodeTripleContext):
        pass


    # Enter a parse tree produced by CypherParser#node.
    def enterNode(self, ctx:CypherParser.NodeContext):
        pass

    # Exit a parse tree produced by CypherParser#node.
    def exitNode(self, ctx:CypherParser.NodeContext):
        pass


    # Enter a parse tree produced by CypherParser#relationship.
    def enterRelationship(self, ctx:CypherParser.RelationshipContext):
        pass

    # Exit a parse tree produced by CypherParser#relationship.
    def exitRelationship(self, ctx:CypherParser.RelationshipContext):
        pass


    # Enter a parse tree produced by CypherParser#constraint.
    def enterConstraint(self, ctx:CypherParser.ConstraintContext):
        pass

    # Exit a parse tree produced by CypherParser#constraint.
    def exitConstraint(self, ctx:CypherParser.ConstraintContext):
        pass


    # Enter a parse tree produced by CypherParser#attribute.
    def enterAttribute(self, ctx:CypherParser.AttributeContext):
        pass

    # Exit a parse tree produced by CypherParser#attribute.
    def exitAttribute(self, ctx:CypherParser.AttributeContext):
        pass


    # Enter a parse tree produced by CypherParser#var.
    def enterVar(self, ctx:CypherParser.VarContext):
        pass

    # Exit a parse tree produced by CypherParser#var.
    def exitVar(self, ctx:CypherParser.VarContext):
        pass


    # Enter a parse tree produced by CypherParser#string.
    def enterString(self, ctx:CypherParser.StringContext):
        pass

    # Exit a parse tree produced by CypherParser#string.
    def exitString(self, ctx:CypherParser.StringContext):
        pass



del CypherParser