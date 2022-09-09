from zlisp import lexer
from zlisp import token
from zlisp import node


class Parser:
    def __init__(self, text=""):
        self.lexer = lexer.Lexer(text)

    def parse(self):
        tok = self.lexer.next_token
        match tok.type:
            case lexer.INT:
                return self._parse_int(tok)
            case lexer.IDENTIFIER:
                return self._parse_id(tok)
            case lexer.EOF:
                return None
            case lexer.EOL:
                return self.parse()
            case lexer.LPAREN:
                return self._parse_expr(tok)
            case lexer.RPAREN:
                return -1

    def _parse_int(self, tok):
        negative = tok.value[0] == "-"
        if negative:
            baseSpec = tok.value[1:3]
        else:
            baseSpec = tok.value[0:2]
        base = 16 if baseSpec == "0x" else 2 if baseSpec == "0b" else 10
        if base == 10:
            num = tok.value
        elif negative:
            num = "-" + tok.value[3:]
        else:
            num = tok.value[2:]
        return node.IntNode(int(num, base))

    def _parse_id(self, tok):
        return node.LiteralNode(tok.value)

    def _parse_expr(self, tok):
        retNode = node.MultipleNode()
        while (subnode := self.parse()) != -1:
            retNode.add(subnode)
        return retNode
