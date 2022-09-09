from zlisp import token


def test_token_without_value():
    tok = token.Token("test")

    assert tok.type == "test"
    assert tok.value is None


def test_token_with_value():
    tok = token.Token("test", 4)

    assert tok.type == "test"
    assert tok.value == 4


def test_token_equality():
    tok1 = token.Token("test", 4)
    tok2 = token.Token("test", 2)
    tok3 = token.Token("test!", 4)
    tok4 = token.Token("test!", 2)
    tok5 = token.Token("test", 4)

    assert tok1 != tok2
    assert tok1 != tok3
    assert tok1 != tok4
    assert tok1 == tok5


def test_token_str():
    tok = token.Token("test", 4)

    assert str(tok) == "('test', 4)"


def test_token_repr():
    tok = token.Token("test", 4)

    assert repr(tok) == "('test', 4)"
