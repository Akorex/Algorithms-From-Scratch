class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def addNode(self, val):
        root = self
        while root.next is not None:
            root = root.next
        root.next = Node(val)

    def iterateLL(self):
        root = self
        print
        while root is not None:
            print(str(root.val) + " ", end="")
            root = root.next
        print()

if __name__ =="__main__":
    L = Node(1)
    L.addNode(2)
    L.addNode(3)
    L.addNode(4)

    # iterate through list and print:
    L.iterateLL()

    # changing value of pointer does not affect L
    P = L
    P = P.next
    L.iterateLL() # L is unchanged


    # changing "next" value of pointer does affect L
    P = L 
    P.next = P.next.next
    L.iterateLL() # now we've skipped node 2

    # changing data of pointer does affect L
    P = L
    P.val = 10
    L.iterateLL()