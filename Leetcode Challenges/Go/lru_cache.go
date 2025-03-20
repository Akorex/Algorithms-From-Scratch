type Node struct {
	key   int
	value int
	prev  *Node
	next  *Node
}

type LRUCache struct {
	capacity int
	cache    map[int]*Node
	head     *Node
	tail     *Node
}

func Constructor(capacity int) LRUCache {
	head, tail := &Node{}, &Node{}
	head.next = tail
	tail.prev = head

	return LRUCache{
		capacity: capacity,
		cache:    make(map[int]*Node),
		head:     head,
		tail:     tail,
	}

}

func (this *LRUCache) Get(key int) int {
	if node, found := this.cache[key]; found {
		this.moveToFront(node)
		return node.value
	}

	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if node, found := this.cache[key]; found {
		node.value = value
		this.moveToFront(node)
	} else {
		if len(this.cache) >= this.capacity {
			this.removeLRU()
		}

		newNode := &Node{key: key, value: value}
		this.cache[key] = newNode
		this.addToFront(newNode)
	}
}

func (this *LRUCache) moveToFront(node *Node) {
	this.removeNode(node)
	this.addToFront(node)
}

func (this *LRUCache) addToFront(node *Node) {
	node.next = this.head.next
	node.prev = this.head
	this.head.next.prev = node
	this.head.next = node
}

func (this *LRUCache) removeNode(node *Node) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (this *LRUCache) removeLRU() {
	if this.tail.prev != this.head {
		lru := this.tail.prev
		delete(this.cache, lru.key) // Delete from cache
		this.removeNode(lru)        // Remove from linked list
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */