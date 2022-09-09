from zlisp import text_buffer
from zlisp import token
import re

EOF = "EOF"
EOL = "EOL"
LPAREN = "("
RPAREN = ")"
INT = "INT"
IDENTIFIER = "IDENTIFIER"


match_int = re.compile(r"\-?((0x[0-9a-fA-F]+)|(0b[01]+)|([0-9]+))")
match_id = re.compile(r"[a-zA-Z_][a-zA-Z_0-9]*")

op_builtins = [
    '+', '-', '*', '/', '%',
    '==', '>=', '<=', '>', '<', '!=',
    "exit", "defvar"
]


class Lexer:
    def __init__(self, txt=None):
        self.text_buffer = text_buffer.TextBuffer(txt)

    @property
    def next_token(self):
        try:
            tok, numSkip = self._tokenize()
            self.text_buffer.skip(numSkip)
            return tok
        except text_buffer.EOFError:
            return token.Token(EOF)
        except text_buffer.EOLError:
            self.text_buffer.next_line()
            return token.Token(EOL)

    def _tokenize(self):
        if self.text_buffer.current_char in " \t":
            self.text_buffer.skip(1)
            return self._tokenize()
        tryParen = self._try_tokenize_paren()
        if tryParen is not None:
            return tryParen

        tryInt = self._try_tokenize_int()
        if tryInt is not None:
            return tryInt

        tryId = self._try_tokenize_identifier()
        if tryId is not None:
            return tryId

        raise ValueError("Unknown token: '{}' (Line {}, col {})"
                         .format(
                            self.text_buffer.current_char,
                            self.text_buffer.line,
                            self.text_buffer.column
                            )
                         )

    def _try_tokenize_identifier(self):
        if self.text_buffer.tail[:2] in op_builtins:
            return token.Token(IDENTIFIER, self.text_buffer.tail[:2]), 2
        elif self.text_buffer.current_char in op_builtins:
            return token.Token(IDENTIFIER, self.text_buffer.current_char), 1

        match = match_id.match(self.text_buffer.tail)
        if match is not None:
            return token.Token(IDENTIFIER, match[0]), match.span(0)[1]

    def _try_tokenize_int(self):
        match = match_int.match(self.text_buffer.tail)
        if match is not None:
            return token.Token(INT, match[0]), match.span(0)[1]

    def _try_tokenize_paren(self):
        if self.text_buffer.current_char == "(":
            return token.Token(LPAREN), 1
        elif self.text_buffer.current_char == ")":
            return token.Token(RPAREN), 1
        return None
