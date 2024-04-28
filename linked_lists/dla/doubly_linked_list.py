class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedLists:

    def __init__(self) -> None:

        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self):
        pass

    def traverse(self):
        tempNode = self.head

        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next

    def reverse(self):
        tempNode = self.tail

        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.prev

    def insertion(self, value, location):
        if self.head is None:
            return "Empty"
            # newNode = Node(value)
            # newNode.next = newNode
            # self.head = newNode
            # self.tail = newNode
            # print("here")
            # return "Created"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.prev = self.tail
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                idx = 0
                while idx < location - 1:
                    tempNode = tempNode.next
                    idx += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode


myDLL = DoublyLinkedLists()
print([node.value for node in myDLL])
node1 = Node(3)
myDLL.head = node1
myDLL.tail = node1

myDLL.insertion(4, 0)

print([node.value for node in myDLL])
myDLL.insertion(40, -1)

print([node.value for node in myDLL])

myDLL.insertion(400, 2)

print([node.value for node in myDLL])


print(myDLL.traverse())
print("--")
print(myDLL.reverse())
