class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        next_node.prev = node
        node.next = next_node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

# Code tests

# Create an LRUCache with capacity 2
lru_cache = LRUCache(2)

# Perform put operations
lru_cache.put(1, 1)  # Cache is {1=1}
lru_cache.put(2, 2)  # Cache is {1=1, 2=2}

# Perform get operations
print(lru_cache.get(1))  # Returns 1, Cache is {2=2, 1=1}

# Perform another put operation, which causes an eviction
lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, Cache is {1=1, 3=3}

# Perform get operations
print(lru_cache.get(2))  # Returns -1 (not found)
print(lru_cache.get(3))  # Returns 3, Cache is {1=1, 3=3}

# Perform another put operation, which causes an eviction
lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, Cache is {3=3, 4=4}

# Perform get operations
print(lru_cache.get(1))  # Returns -1 (not found)
print(lru_cache.get(3))  # Returns 3, Cache is {3=3, 4=4}
print(lru_cache.get(4))  # Returns 4, Cache is {3=3, 4=4}
