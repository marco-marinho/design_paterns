"""
The interpreter is a design pattern used to turn strings into object representations. It is usually done in two steps,
lexing and parsing.

The interpreter design pattern is a behavioral pattern that defines a grammar for a language and uses an interpreter to
interpret sentences in the language. This pattern is particularly useful for implementing simple languages or
expressions, where it can define the syntax and semantics of a language within a program.

Key Points:
1 - Grammar Representation: The pattern represents the grammar of a language using classes.
2 - Evaluation: Each class in the pattern is responsible for interpreting a specific part of the language.
3 - Abstract Syntax Tree (AST): The pattern often uses an abstract syntax tree to represent expressions in the language,
    where each node is an instance of a class.
4 - Recursive Interpretation: The interpretation process is typically recursive, with each node in the AST interpreting
    itself and its children.

https://blogs.perl.org/users/jeffrey_kegler/2013/03/the-interpreter-design-pattern.html
"""

import regex as re
from enum import Enum, auto

lpar = re.compile(r'^\(')
rpar = re.compile(r'^\)')
plus = re.compile(r'^\+')
minus = re.compile(r'^\-')
integer = re.compile(r'^\d+')


class TokenType(Enum):
    LPAR = auto()
    RPAR = auto()
    PLUS = auto()
    MINUS = auto()
    INTEGER = auto()


class Token:

    def __init__(self, token_type: TokenType, value: str):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"´{self.value}´"


def lex(expression: str):
    expression = expression.replace(" ", "")
    idx = 0
    output = []
    while idx < len(expression):
        if (res := re.search(lpar, expression[idx:])) is not None:
            output.append(Token(TokenType.LPAR, "("))
            idx += res.span()[1]
        elif (res := re.search(rpar, expression[idx:])) is not None:
            output.append(Token(TokenType.RPAR, ")"))
            idx += res.span()[1]
        elif (res := re.search(plus, expression[idx:])) is not None:
            output.append(Token(TokenType.PLUS, "+"))
            idx += res.span()[1]
        elif (res := re.search(minus, expression[idx:])) is not None:
            output.append(Token(TokenType.MINUS, "-"))
            idx += res.span()[1]
        elif (res := re.search(integer, expression[idx:])) is not None:
            output.append(Token(TokenType.INTEGER, res.group()))
            idx += res.span()[1]
    return output


def parse(tokens: list[Token]):
    lhv = None
    rhv = None
    op = None
    idx = 0

    while idx < len(tokens):
        match tokens[idx].type:
            case TokenType.LPAR:
                end_par = next(i for i, element in enumerate(tokens[idx:]) if element.type == TokenType.RPAR)
                value = parse(tokens[idx + 1: idx + end_par])
                idx = end_par
                if lhv is None:
                    lhv = value
                else:
                    rhv = value
            case TokenType.INTEGER:
                value = int(tokens[idx].value)
                if lhv is None:
                    lhv = value
                else:
                    rhv = value
            case TokenType.PLUS:
                op = TokenType.PLUS
            case TokenType.MINUS:
                op = TokenType.MINUS
        idx += 1
    if op == TokenType.PLUS:
        return lhv + rhv
    elif op == TokenType.MINUS:
        return lhv - rhv


if __name__ == "__main__":
    inn = "(12 + 34) - 10"
    tokens = lex(inn)
    print(parse(tokens))
