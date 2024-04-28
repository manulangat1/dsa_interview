import random


class Stack:

    def __init__(self) -> None:
        self.list = []
        self.size = 9

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        return True if self.list == [] else False

    def isFull(self):
        return True if len(self.list) == self.size else False

    def push(self, value):
        if self.isFull():
            return "This is full"
        return self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "Empty"
        return self.list.pop()


myStack = Stack()

print(myStack)

for _ in range(8):
    myStack.push(random.randint(_, 99))

print(myStack)
print("--->")
print(myStack.pop())
