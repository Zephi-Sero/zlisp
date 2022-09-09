from zlisp import node

class Function:
    def __init__(self, name="", args=[], definition=[]):
        self.name = name
        self.args = args
        self.definition = definition


class Variable:
    def __init__(self, name="", value=None):
        self.type = "int"
        self.name = name
        self.value = value


class Context:
    def __init__(self, vars={}, funs={}):
        self.vars = vars
        self.funs = funs


def _py_eval(context, text=""):
    eval(text, 
