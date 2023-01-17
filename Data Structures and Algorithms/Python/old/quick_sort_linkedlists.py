from linked_lists import LinkedQueue

def quick_sort(S):
    """Sort the elements of a queue S using the quick sort algorithm"""
    n = len(S)
    if n < 2:
        return # queue trivially sorted
    
    # divide
    p = S.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif S.first() > p:
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())


    # conquer (with recursion)
    quick_sort(L)
    quick_sort(G)

    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())