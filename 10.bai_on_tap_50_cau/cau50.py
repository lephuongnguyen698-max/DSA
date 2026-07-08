class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * size

    def h1(self, x):
        return hash(x) % self.size

    def h2(self, x):
        return (hash(x) * 7) % self.size

    def add(self, x):
        self.bits[self.h1(x)] = 1
        self.bits[self.h2(x)] = 1

    def check(self, x):
        return self.bits[self.h1(x)] and self.bits[self.h2(x)]

bf = BloomFilter(20)

bf.add("apple")
bf.add("banana")

print(bf.check("apple"))
print(bf.check("banana"))
print(bf.check("orange"))