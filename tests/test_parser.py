from zlisp import parser
from zlisp import node


def test_parser_understands_eof():
    par = parser.Parser("")

    assert par.parse() is None


def test_parser_understands_eol():
    par = parser.Parser("\n")

    assert par.parse() is None


def test_parser_understands_int():
    par = parser.Parser("42")

    assert par.parse() == node.IntNode(42)


def test_parser_understands_id():
    par = parser.Parser("abc")

    assert par.parse() == node.LiteralNode("abc")


def test_parser_understands_expr():
    par = parser.Parser("(+ 2 4)")

    assert par.parse() == node.MultipleNode(
                                                node.LiteralNode("+"),
                                                node.IntNode(2),
                                                node.IntNode(4)
                                           )


def test_parser_understands_unnecessary_nesting():
    par = parser.Parser("((+ 2 4))")

    assert par.parse() == node.MultipleNode(node.MultipleNode(
                                                node.LiteralNode("+"),
                                                node.IntNode(2),
                                                node.IntNode(4)
                                           ))


def test_parser_understands_int_hex():
    par = parser.Parser("0x22")

    assert par.parse() == node.IntNode(0x22)


def test_parser_understands_int_negative_binary():
    par = parser.Parser("-0b1001")

    assert par.parse() == node.IntNode(-0b1001)
