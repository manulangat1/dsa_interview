# determine if 2 LL intersect , return the intersecting node
"""
the intersection is defined based on referance not value ie if the kth node of the 1st LL is the exact same node 
 (by referance ) as the jth node of the second linked list then they are intersecting. 

- 2 intersecting LL will always have the same last node. 
- 1st option is to traverse through them at the same time and when they collide they it is intersection, ie if they are the same LL. 
- if not of the same legth then ignore the rest of the other ones. 

"""

from practise import LL, Node


def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shortNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shortNode is not longerNode:
        shortNode = shortNode.next
        longerNode = longerNode.next

    return shortNode


# helper addition method


def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LL()
llA.generate(3, 0, 10)
llB = LL()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))
# time comp is O ( A + B )
