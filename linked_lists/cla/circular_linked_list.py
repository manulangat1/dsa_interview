class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class CircularLinkedList:

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

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL is created"

    def traverse(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break

    def search(self, value):
        node = self.head

        while node:
            if node.value == value:
                return node.value
            node = node.next
            if node == self.tail.next:
                return " Node does not exist"
                # break
        # return "Not found"

    def insertion(self, value, location):
        """
        Insertion can occur at
        1. The beginning og the linked list
        2. Specified location of the list
        3. end of the linked list
        assumptions made below. 1. That a linked list is already created.
        """
        newNode = Node(value)
        print(newNode)
        if location == 0:
            newNode.next = self.head
            self.head = newNode
            print("done")
            return "done"
        elif location == -1:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
        else:
            index = 0
            tempNode = self.head
            while index < location - 1:
                index += 1
                tempNode = tempNode.next

                if tempNode == self.tail.next:
                    break
            print(index, location)
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode

        return "done"


myCSLL = CircularLinkedList()
myCSLL.createCSLL(10)
print([node.value for node in myCSLL])
myCSLL.insertion(2, 0)
print([node.value for node in myCSLL])
myCSLL.insertion(5, 0)
print([node.value for node in myCSLL])

myCSLL.insertion(5, -1)
print([node.value for node in myCSLL])

myCSLL.insertion(500, 2)
print([node.value for node in myCSLL])

print(myCSLL.traverse())

print("----")

print(myCSLL.search(5))
