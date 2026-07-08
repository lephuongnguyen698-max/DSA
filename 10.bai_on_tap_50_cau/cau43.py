class ResizableHashTable:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity

    def _hash(self, key, capacity):
        return hash(key) % capacity

    def _rehash(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity
        
        for bucket in self.table:
            if bucket:
                for key, value in bucket:
                    idx = self._hash(key, new_capacity)
                    if not new_table[idx]:
                        new_table[idx] = []
                    new_table[idx].append((key, value))
                    
        self.capacity = new_capacity
        self.table = new_table

    def put(self, key, value):
        idx = self._hash(key, self.capacity)
        if not self.table[idx]:
            self.table[idx] = []
            
        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                self.table[idx][i] = (key, value)
                return
                
        self.table[idx].append((key, value))
        self.size += 1
        
        if self.size / self.capacity > 0.75:
            self._rehash()

    def get(self, key):
        idx = self._hash(key, self.capacity)
        if self.table[idx]:
            for k, v in self.table[idx]:
                if k == key:
                    return v
        return None

ht = ResizableHashTable()
ht.put("a", 1)
ht.put("b", 2)
ht.put("c", 3)
ht.put("d", 4)
print(ht.capacity)