"""
The visitor design pattern is a behavioral pattern that allows you to add further operations to objects without having
to modify them. It separates an algorithm from the object structure it operates on by moving the algorithm into a
visitor object.

Key Points:
1 - Separation of Concerns: Separates the operations from the objects on which they operate.
2 - Double Dispatch: Uses double dispatch to execute the appropriate method on a visitor object.
3 - Extensibility: Makes it easy to add new operations without changing the classes of the elements on
    which it operates.
4 - Object Structure: Suitable for structures with many distinct and unrelated operations to perform.

https://refactoring.guru/design-patterns/visitor
"""

from multimethod import multimethod


class DoubleNode:
    def __init__(self, value: int):
        self.value = value


class AdditionNode:

    def __init__(self, left: DoubleNode, right: DoubleNode):
        self.left = left
        self.right = right


class NodePrinter:

    @multimethod
    def visit(self, node: DoubleNode):
        return str(node.value)

    @visit.register
    def _(self, node: AdditionNode):
        return f"({self.visit(node.left)} + {self.visit(node.right)})"


class NodeEvaluator:

    @multimethod
    def visit(self, node: DoubleNode):
        return node.value

    @visit.register
    def _(self, node: AdditionNode):
        return self.visit(node.left) + self.visit(node.right)


if __name__ == "__main__":
    left = DoubleNode(2)
    right = DoubleNode(3)
    addition = AdditionNode(left, right)

    printer = NodePrinter()
    evaluator = NodeEvaluator()

    print(printer.visit(addition))
    print(evaluator.visit(addition))
