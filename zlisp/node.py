class Node:
    type = "node"

    def __init__(self):
        pass

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.type == other.type

    def asdict(self):
        return {"type": self.type}

    def __str__(self):
        return str(self.asdict())

    def __repr__(self):
        return repr(self.asdict())


class ValueNode(Node):
    value = None

    def __init__(self, value=None):
        self.value = value
        self.type = "value"

    def asdict(self):
        return {"type": self.type, "value": self.value}

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.type, self.value == other.type, other.value


class IntNode(ValueNode):
    def __init__(self, value=0):
        super().__init__(value)
        self.type = "int"


class LiteralNode(ValueNode):
    def __init__(self, value=""):
        super().__init__(value)
        self.type = "literal"


class MultipleNode(ValueNode):
    def __init__(self, *args):
        super().__init__(list(args))
        self.type = "multiple"

    def add(self, value):
        self.value.append(value)
