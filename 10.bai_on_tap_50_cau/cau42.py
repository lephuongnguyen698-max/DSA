class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        if not self.table[idx]:
            self.table[idx] = Node(key, value)
            return
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                curr.value = value
                return
            if not curr.next:
                break
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def remove(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[idx] = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.deleted = [False] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        start_idx = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + 1) % self.size
            if idx == start_idx:
                return
        self.keys[idx] = key
        self.values[idx] = value
        self.deleted[idx] = False

    def get(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.keys[idx] is not None or self.deleted[idx]:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return None

    def remove(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.keys[idx] is not None or self.deleted[idx]:
            if self.keys[idx] == key:
                self.keys[idx] = None
                self.values[idx] = None
                self.deleted[idx] = True
                return True
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return False

ht_chain = ChainingHashTable()
ht_chain.put("key1", "val1")
print(ht_chain.get("key1"))

ht_linear = LinearProbingHashTable()
ht_linear.put("key1", "val1")
print(ht_linear.get("key1"))