from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def eat(self, token_type):
        if self.tokens[self.pos][0] == token_type:
            self.pos += 1
        else:
            raise Exception("Unexpected token")

    def factor(self):
        token = self.tokens[self.pos]
        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return Number(token[1])
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node

    def term(self):
        node = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('MUL', 'DIV'):
            op = self.tokens[self.pos][1]
            self.eat(self.tokens[self.pos][0])
            node = BinOp(node, op, self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('PLUS', 'MINUS'):
            op = self.tokens[self.pos][1]
            self.eat(self.tokens[self.pos][0])
            node = BinOp(node, op, self.term())
        return node