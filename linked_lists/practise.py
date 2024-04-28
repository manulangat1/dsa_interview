import random


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)


class LL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        if self.head is None:
            return "Empty list"
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                break

    def __str__(self) -> str:
        values = [str(x.value) for x in self]
        return "-->".join(values)

    def __len__(self):
        value = 0
        node = self.head
        while node:
            value += 1
            node = node.next
            if node == self.tail.next:
                break
        return value

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:

            # newNode.prev = self.tail
            # newNode.next = self.head
            # self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode
            return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None

        for i in range(n):
            self.add(random.randint(min_value, max_value))
        return self


myL1 = LL()
myL1.add(5)
print(len(myL1))
print(myL1)
myL1.generate(10, 0, 99)
print(myL1)
