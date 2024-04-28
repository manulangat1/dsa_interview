# write code to partition a linked list around a value x such that all nodes less than x comes before all nodes greater than or equal to x
from practise import LL


def partition(ll, n):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        ll.tail = ll.head

        while currNode:
            nextNode = currNode.next
            currNode.next = None
            if currNode.value < n:
                currNode.next = ll.head
                ll.head = currNode
            else:
                ll.tail.next = currNode
                ll.tail = currNode
            currNode = nextNode
        if ll.tail.next is not None:
            ll.tail.next = None
        return ll


myDup = LL()
myDup.generate(10, 2, 99)
print(myDup)
print("-->")
# removeDups(myDup)
print(partition(myDup, 50))
print("-->")
print(myDup)
