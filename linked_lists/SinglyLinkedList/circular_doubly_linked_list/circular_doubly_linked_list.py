class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class CDLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def insert(self, value, location):
        if self.head is None:
            return "This is an empty LL "
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                idx = 0
                tempNode = self.head
                while idx < location - 1:
                    tempNode = tempNode.next
                    idx += 1
                    if tempNode == self.tail.next:
                        break
                print(idx, location)
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

        return "Added"


node1 = Node(5)
node1.next = node1
node1.prev = node1
myCl = CDLL()
print(myCl.insert(0, 1))
myCl.head = node1
myCl.tail = node1

print([node.value for node in myCl])

print(myCl.insert(10, 0))
print([node.value for node in myCl])
print(myCl.insert(100, -1))
print([node.value for node in myCl])
print(myCl.insert(1000, 1))
print([node.value for node in myCl])
