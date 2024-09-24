from linked_list import LinkedList


def kth_to_last(ll, k):
    leader = ll.head
    follower = ll.head
    count = 0

    while leader:
        if count >= k:
            follower = follower.next
        count += 1
        leader = follower.next
    return follower