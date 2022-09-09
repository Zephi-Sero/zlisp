from zlisp import node
from zlisp import lexer


class Visitor:
    def __init__(self):
        self.onExit = exit
        self.funs = {}
        self.vars = {}

    def set_onExit(self, func):
        self.onExit = func

    def visit(self, ast=node.Node()):
        if ast is None:
            return None
        if ast.type == "node":
            return None
        elif ast.type == "int":
            return ast.value
        elif ast.type == "literal":
            return ast.value
        elif ast.type == "multiple":
            v = self._visit_multiple(ast)
            return v

    def _visit_multiple(self, ast):
        if len(ast.value) == 1 and type(ast.value[0]) is node.MultipleNode:
            return self._visit_multiple(ast.value[0])
        elif self.visit(ast.value[0]) in lexer.op_builtins:
            return self._run_op(ast)

    def _run_op(self, ast):
        op = self.visit(ast.value[0])
        args = ast.value[1:]
        if len(args) == 1:
            arg = self.visit(args[0])
            if op == "exit":
                self.onExit(arg)
                return None
            elif op == "-":
                return -arg
        elif len(args) == 2:
            left = self.visit(args[0])
            right = self.visit(args[1])
            match op:
                case "+":
                    return left + right
                case "-":
                    return left - right
                case "*":
                    return left * right
                case "/":
                    return left // right
                case "%":
                    return left % right
                case ">":
                    return 1 if left > right else 0
                case "<":
                    return 1 if left < right else 0
                case "==":
                    return 1 if left == right else 0
                case "!=":
                    return 1 if left != right else 0
                case ">=":
                    return 1 if left >= right else 0
                case "<=":
                    return 1 if left <= right else 0
                case "defvar":
                    return right
