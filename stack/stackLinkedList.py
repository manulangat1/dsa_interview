import random


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class SLL:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        if self.head is None:
            return "empty"
        tempNode = self.head
        while tempNode is not None:
            yield tempNode
            tempNode = tempNode.next


class Stack:
    def __init__(self) -> None:
        self.LinkedList = SLL()

    def __str__(self) -> str:
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)

    def isEmpty(self):
        return True if self.LinkedList.head is None else False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "Empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


myStack = Stack()
print(myStack)
for _ in range(9):
    myStack.push(random.randint(_, 1008))

print(myStack)
print("<--->")
print(myStack.pop())
print("<--->")
print(myStack)
print("<--->")
print(myStack.peek())
print("<--->")
myStack.delete()
print(myStack)
