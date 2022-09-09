from zlisp import visitor
from zlisp import parser
from zlisp import node


def test_visitor_understands_int():
    vis = visitor.Visitor()
    par = parser.Parser("2")

    assert vis.visit(par.parse()) == 2


def test_visitor_understands_empty_node():
    vis = visitor.Visitor()

    assert vis.visit(node.Node()) is None


def test_visitor_understands_expr():
    vis = visitor.Visitor()
    par = parser.Parser("(+ 2 4)")

    assert vis.visit(par.parse()) == 6


def test_visitor_understands_eol():
    vis = visitor.Visitor()
    par = parser.Parser("\n(+ 2 4)")

    assert vis.visit(par.parse()) == 6


def test_visitor_understands_eof():
    vis = visitor.Visitor()
    par = parser.Parser()

    assert vis.visit(par.parse()) is None


def test_visitor_understands_arith_ops():
    vis = visitor.Visitor()
    par = parser.Parser("(+ 2 4)\n(* 8 2)\n(/ 4 2)\n(- 4 1)\n(% 3 2)")

    assert vis.visit(par.parse()) == 6
    assert vis.visit(par.parse()) == 16
    assert vis.visit(par.parse()) == 2
    assert vis.visit(par.parse()) == 3
    assert vis.visit(par.parse()) == 1


def test_visitor_understands_compare_ops():
    vis = visitor.Visitor()
    par = parser.Parser(
            "(== 2 2)\n(> 8 2)\n(< 2 1)\n(!= 6 6)\n(>= 3 2)\n(<= 84 55)"
                       )

    assert vis.visit(par.parse()) == 1
    assert vis.visit(par.parse()) == 1
    assert vis.visit(par.parse()) == 0
    assert vis.visit(par.parse()) == 0
    assert vis.visit(par.parse()) == 1
    assert vis.visit(par.parse()) == 0


def test_visitor_understands_nested_expr():
    vis = visitor.Visitor()
    par = parser.Parser("(+ 2 (* 8 6))")

    assert vis.visit(par.parse()) == 50


def test_visitor_understands_unnecessary_nest():
    vis = visitor.Visitor()
    par = parser.Parser("((+ 2 4))")

    assert vis.visit(par.parse()) == 6


def test_visitor_understands_exit():
    global v
    v = 0

    def onExit(code):
        global v
        v = code + 4

    vis = visitor.Visitor()
    par = parser.Parser("(exit 24)")
    vis.set_onExit(onExit)

    assert vis.visit(par.parse()) is None
    assert v == 28


def test_visitor_understands_unary_minus():
    vis = visitor.Visitor()
    par = parser.Parser("(- 8)")

    assert vis.visit(par.parse()) == -8


def test_visitor_understands_defvar():
    vis = visitor.Visitor()
    par = parser.Parser("(defvar x 24)")

    assert vis.visit(par.parse()) == 24
#    assert vis.visit(par.parse()) == 28
