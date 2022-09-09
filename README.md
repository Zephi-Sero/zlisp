# Z's Lisp Interpreter

## Math

`(+ 2 (* 8 4))` will multiply 8 and 4, then add 2.

## Built-in Functions

Currently, there is only `+` `-` `*` `/` `%` for arithmetic. There are also comparison
operators `>` `<` `==` `!=` `>=` `<=`. These return 1 if the left side has the corresponding
relation with the right side. Otherwise, they return 0. For example:

`(>= 2 4)` will return 0, because 2 is not >= 4.

There is also a function `exit` which exits with the exit code specified by
its first argument.

`(exit (+ 2 4))` causes the zlisp REPL to exit with a code of 6.
