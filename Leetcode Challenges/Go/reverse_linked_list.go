package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {

	var prev *ListNode
	curr := head

	for curr != nil {
		nextNode := curr.Next

		curr.Next = prev //reverses the link

		prev = curr
		curr = nextNode
	}

	return prev
}
