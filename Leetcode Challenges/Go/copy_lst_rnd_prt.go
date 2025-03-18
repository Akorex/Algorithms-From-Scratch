package main

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}

	hashMap := map[*Node]*Node{}
	curr := head

	for curr != nil {
		hashMap[curr] = &Node{Val: curr.Val}
		curr = curr.Next
	}

	curr = head
	for curr != nil {
		copiedNode := hashMap[curr]
		copiedNode.Next = hashMap[curr.Next]
		copiedNode.Random = hashMap[curr.Random]
		curr = curr.Next
	}

	return hashMap[head]

}
