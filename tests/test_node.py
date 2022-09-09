from zlisp import node


def test_node_empty():
    n = node.Node()

    assert n.asdict() == {"type": "node"}
    assert str(n) == str({"type": "node"})
    assert repr(n) == repr({"type": "node"})


def test_node_value():
    n = node.ValueNode("hello")

    assert n.asdict() == {"type": "value", "value": "hello"}


def test_node_int():
    n = node.IntNode(4)

    assert n.asdict() == {"type": "int", "value": 4}


def test_node_literal():
    n = node.LiteralNode("abc")

    assert n.asdict() == {"type": "literal", "value": "abc"}


def test_node_multiple():
    n = node.MultipleNode(
                          node.LiteralNode("+"),
                          node.IntNode(4),
                          node.IntNode(2)
                         )

    assert n.asdict() == {
                            "type": "multiple",
                            "value": [
                                node.LiteralNode("+"),
                                node.IntNode(4),
                                node.IntNode(2)
                            ]
                         }


def test_node_empty_equality():
    n1 = node.Node()
    n2 = node.Node()

    assert n1 == n2
    assert n1 != 4


def test_node_multiple_add():
    n = node.MultipleNode(node.LiteralNode("+"))

    n.add(node.IntNode(4))

    assert n.asdict() == {
                            "type": "multiple",
                            "value": [
                                node.LiteralNode("+"),
                                node.IntNode(4)
                            ]
                       }
