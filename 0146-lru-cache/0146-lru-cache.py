class LRUCache:
    class ListNode:
        def __init__(self):
            self.val = None
            self.key = None
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    # remove the entry from the linked list()
    def delete(self, node):
        prev = node.prev
        node.next.prev = prev
        prev.next = node.next

    def add(self, node):

        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode
        self.tail.prev = node
        node.next = self.tail

    # add the entry to the linked list

    def get(self, key: int) -> int:
        # if not present return -1
        # if yes, upadate the usage by geting the existing key and value
        # then delete the pair and then again add it to the cache, only need to update linked list()
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.delete(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if already exists the the key update its value by first removing it
        # then add it to the cache i.e. linked list()
        # then if the size becomes more than the capacity remove the head and move head next
        node = ListNode()
        node.val = value
        node.key = key
        if key in self.cache:
            self.delete(self.cache[key])

        self.add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            del self.cache[lru_node.key]
            self.delete(lru_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
