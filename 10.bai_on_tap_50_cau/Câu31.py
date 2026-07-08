class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, item):
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
            
        self.array[self.size] = item
        self.size += 1

arr = DynamicArray()
for i in range(5):
    arr.append(i)
print(arr.array[:arr.size])