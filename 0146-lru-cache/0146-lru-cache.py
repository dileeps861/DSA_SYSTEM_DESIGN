class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail 
        self.capacity = capacity

    def insert(self, node):
        oldNode = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        oldNode.next = node
        node.prev = oldNode

    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].value
        

    def put(self, key: int, value: int) -> None:
        node = Node(value, key)
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = node
        self.insert(node)
        
        if len(self.cache) > self.capacity:
            del self.cache[self.head.next.key]
            self.remove(self.head.next)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)