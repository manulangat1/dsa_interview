#  remove duplicates from linked list
# you can use a set
from practise import LL


def removeDups(ll):
    if ll.head is None:  # O(1)
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])

        while currentNode.next:  # 0 (n)
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll


def removeDup1(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next

    return ll


myDup = LL()
myDup.generate(10, 2, 4)
print(myDup)
print("-->")
# removeDups(myDup)
removeDup1(myDup)
print(myDup)
