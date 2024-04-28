from practise import LL


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head

    curry = 0

    ll = LL()

    while n1 or n2:
        result = curry

        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(int(result % 10))
        curry = result / 10

    return ll


myDup = LL()
myDup.generate(10, 2, 99)

myDup2 = LL()
myDup2.generate(10, 2, 99)
print(myDup, "--> llA")
print(myDup2, "--> llB")
print("-->")
# removeDups(myDup)
print(sumList(myDup, myDup2))
print("-->")
# print(myDup)
