# n steps from the last element
from practise import LL


def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


myDup = LL()
myDup.generate(10, 2, 99)
print(myDup)
print("-->")
# removeDups(myDup)
print(nthToLast(myDup, 4))
# print(myDup)
