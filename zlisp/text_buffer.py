class EOLError(ValueError):
    """ Signals that the buffer is reading past a line """


class EOFError(ValueError):
    """ Signals that the buffer is reading past end of the text """


class TextBuffer:
    def __init__(self, txt=None):
        self.load(txt)

    def load(self, txt):
        if txt is None or txt == "":
            self.lines = []
        else:
            self.lines = txt.split("\n")
        self.reset()

    def reset(self):
        self.line = 0
        self.column = 0

    def skip(self, count=1):
        self.column += count

    def next_line(self):
        self.goto(self.line + 1)

    def goto(self, line, column=0):
        self.line = line
        self.column = column

    @property
    def current_char(self):
        try:
            return self.current_line[self.column]
        except EOFError as e:
            raise e
        except IndexError:
            raise EOLError("EOL reading line {}, column {}"
                           .format(self.line, self.column)
                           )

    @property
    def current_line(self):
        try:
            return self.lines[self.line]
        except IndexError:
            raise EOFError("EOF reading line {}"
                           .format(self.line)
                           )

    @property
    def head(self):
        return self.current_line[:self.column]

    @property
    def tail(self):
        return self.current_line[self.column:]
