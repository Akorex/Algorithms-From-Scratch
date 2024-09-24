from linked_list import LinkedList

def remove_dups(ll):
    current = ll.head
    prev = None
    seen = set()

    while current:
        if current.value in seen:
            prev.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll

# using two pointers
def remove_dups_twopointer(ll):
    runner = current = ll.head

    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = current.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll