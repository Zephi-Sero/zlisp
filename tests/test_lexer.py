from zlisp import lexer
from zlisp import token
import pytest


def test_lexer_empty():
    lex = lexer.Lexer()

    assert lex.text_buffer.lines == []


def test_lexer_understands_eof():
    lex = lexer.Lexer()

    assert lex.next_token == token.Token(lexer.EOF)


def test_lexer_understands_eol():
    lex = lexer.Lexer("\n")

    assert lex.next_token == token.Token(lexer.EOL)


def test_lexer_understands_whitespace():
    lex = lexer.Lexer(" \t")

    assert lex.next_token == token.Token(lexer.EOL)


def test_lexer_understands_unknown():
    lex = lexer.Lexer("$")

    with pytest.raises(ValueError):
        lex.next_token


def test_lexer_understands_parentheses():
    lex = lexer.Lexer("()")

    assert lex.next_token == token.Token(lexer.LPAREN)
    assert lex.next_token == token.Token(lexer.RPAREN)


def test_lexer_understands_positive_decimal_int():
    lex = lexer.Lexer("248")

    assert lex.next_token == token.Token(lexer.INT, "248")


def test_lexer_understands_negative_decimal_int():
    lex = lexer.Lexer("-84")

    assert lex.next_token == token.Token(lexer.INT, "-84")


def test_lexer_understands_binary_int():
    lex = lexer.Lexer("0b1001")

    assert lex.next_token == token.Token(lexer.INT, "0b1001")


def test_lexer_understands_hexadecimal_int():
    lex = lexer.Lexer("0x43fc8")

    assert lex.next_token == token.Token(lexer.INT, "0x43fc8")


def test_lexer_understands_builtin_op_single():
    lex = lexer.Lexer("--8")

    assert lex.next_token == token.Token(lexer.IDENTIFIER, "-")
    assert lex.next_token == token.Token(lexer.INT, "-8")


def test_lexer_understands_builtin_op_double():
    lex = lexer.Lexer("==-4")

    assert lex.next_token == token.Token(lexer.IDENTIFIER, "==")
    assert lex.next_token == token.Token(lexer.INT, "-4")


def test_lexer_understands_named_identifier():
    lex = lexer.Lexer("+abc-4")

    assert lex.next_token == token.Token(lexer.IDENTIFIER, "+")
    assert lex.next_token == token.Token(lexer.IDENTIFIER, "abc")
    assert lex.next_token == token.Token(lexer.INT, "-4")
