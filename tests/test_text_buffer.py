import pytest

from zlisp import text_buffer


def test_text_buffer_init_empty():
    tb = text_buffer.TextBuffer()

    with pytest.raises(text_buffer.EOFError):
        tb.current_char


def test_text_buffer_single_line():
    tb = text_buffer.TextBuffer("abcdef")

    assert tb.current_char == "a"
    assert tb.current_line == "abcdef"
    assert tb.line == 0
    assert tb.column == 0
    with pytest.raises(text_buffer.EOFError):
        tb.next_line()
        tb.current_char


def test_text_buffer_skip():
    tb = text_buffer.TextBuffer("abcdef")

    tb.skip(3)

    assert tb.current_char == "d"


def test_text_buffer_multiline():
    tb = text_buffer.TextBuffer("abcdef\nghijkl")

    assert tb.current_line == "abcdef"
    tb.skip(10)
    with pytest.raises(text_buffer.EOLError):
        tb.current_char
    tb.next_line()
    assert tb.current_line == "ghijkl"
    with pytest.raises(text_buffer.EOFError):
        tb.next_line()
        tb.current_line


def test_text_buffer_goto():
    tb = text_buffer.TextBuffer("abcdef\nghijkl\nmnopqrst")

    tb.goto(1, 4)
    assert tb.current_char == "k"


def test_text_buffer_head():
    tb = text_buffer.TextBuffer("abcdef\nghijkl")

    tb.skip(3)
    assert tb.head == "abc"


def test_text_buffer_tail():
    tb = text_buffer.TextBuffer("abcdef\nghijkl")

    tb.skip(3)
    assert tb.tail == "def"
