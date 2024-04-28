# p4mance leaks as size increases

import random


class Stack:

    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        return True if self.list == [] else False

    def push(self, value):
        return self.list.append(value)

    def pop(self):
        # removes  last item and
        if self.isEmpty():
            return "Empty stack"
        return self.list.pop()

    def peek(self):
        #  checks the last
        if self.isEmpty():
            return " There is not any element in stack"
        return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


customStack = Stack()
print(customStack.isEmpty())
for _ in range(10):
    customStack.push(random.randint(_, 99))
print(customStack)

print(customStack.pop())
print(customStack)

print("-->")
print(customStack.peek())
