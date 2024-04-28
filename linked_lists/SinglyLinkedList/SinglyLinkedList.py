class Node: 
    def __init__(self, value= None) -> None:
        self.value =  value  
        self.next = None

class SinglyLinkedList: 

    def __init__(self) -> None:
        self.head = None 
        self.tail = None 

    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next

    def traverse( self):
        """
        check head  else terminate
        loop all nodes and print the value
        """
        if self.head is None: 
            return "empty list"
        tempNode = self.head 

        while tempNode: 
            print( tempNode.value ) 
            tempNode = tempNode.next

    def search(self, searchValue):
        """
        Traverse through the linked list and check whether value is what is looking for else terminate
        """
        tempNode = self.head 
        while tempNode: 
            if tempNode.value == searchValue:
                return "Found" 
            else: 
                tempNode = tempNode.next
                return "The value does not exist"
    def deletion(self, location): 
        """
        1. first node - delete the ref to the head and tail 
        2. 
        """
        if self.head is None: 
            return "Does not exists"
        else: 
            if location == 0 : 
                if self.head == self.tail: 
                    self.head = None 
                    self.tail = None 
                else: 
                    self.head = self.head.next
            elif location == -1: 
                if self.head == self.tail: 
                    self.head = None 
                    self.tail = None 
                else: 
                    tempNode = self.head 
                    while tempNode is not None: 
                        if tempNode.next == self.tail: 
                            break 
                        tempNode = tempNode.next  
                    tempNode.next = None 
                    self.tail = tempNode
            else: 
                tempNode = self.head 
                idx = 0 
                while idx < location -1:
                    tempNode = tempNode.next
                tempNode.next = tempNode.next.next
                # if tempNode
    def deleteEntire(self):
        if self.head is None: 
            print("The SLL does not exist")
        else: 
            self.head = None 
            self.tail = None
                 


    
        

    def insert(self, location, value):
        """
        1. At the beginning of the linked list. 
        2. After a node in the middle of linked list. 
        3. At the end of the linked list.
        """
        pass
        # if self.head is None: 
        #     return "Empty list"
        # newNode = Node(value)

        newNode = Node(value)

        if self.head is None: 
            self.head = newNode 
            self.tail = newNode
            return "Added"
        else: 
            if location == 0: 
                newNode.next = self.head 
                self.head = newNode 
                return "added"
            elif location == -1:

                newNode.next = None
                self.tail.next = newNode 
                self.tail = newNode
            else:
                
                  
                """
                count till the location is found 
                Once location is found,
                """
                count = 0 
                tempNode = self.head 

                while    count< location-1: 
                    tempNode = tempNode.next 
                    count += 1
                print(count) 
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail: 
                    self.tail = newNode
                
                 





myL1 = SinglyLinkedList()
# node1 = Node(1)
# node2 = Node(3)

# myL1.head = node1
# myL1.head.next = node2
# myL1.tail = node2

print([ n.value for n in myL1])
myL1.insert( 0, 100)
print([ n.value for n in myL1])
myL1.insert( 0, 900)
print([ n.value for n in myL1])
myL1.insert( -1, 500)
print([ n.value for n in myL1])
# myL1.insert( -1, 500)
# print([ n.value for n in myL1])
myL1.insert( 2, 600)
print([ n.value for n in myL1])

myL1.traverse()

print(myL1.search(90000))

myL1.deletion(0)
print([ n.value for n in myL1])
myL1.deletion(1)
print([ n.value for n in myL1])
myL1.deletion(1)
print([ n.value for n in myL1])
