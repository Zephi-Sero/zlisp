from zlisp import parser
from zlisp import visitor
import readline


global needsExit
global exitCode
needsExit = False
exitCode = 0


def onExit(code):
    global needsExit
    global exitCode

    needsExit = True
    exitCode = code


def main():
    global needsExit
    global exitCode

    # just to remove annoying import warn
    # -- imported so that arrow keys and home/end
    # work without having to make my own input
    readline.clear_history()

    par = parser.Parser("")
    vis = visitor.Visitor()
    vis.set_onExit(onExit)

    while True:
        try:
            line = input("zlisp > ")
        except EOFError:
            break

        par.lexer.text_buffer.lines.append(line)

        while (ast := par.parse()) is not None:
            result = vis.visit(ast)
            if result is not None:
                print(result)

            if needsExit:
                break

        if needsExit:
            break

    del par
    del vis
    if not needsExit:
        print("(exit {})".format(exitCode))
    exit(exitCode)


if __name__ == '__main__':
    main()
