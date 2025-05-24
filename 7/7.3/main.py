n = int(input())
numbers = list(map(int, input().split()))

class HashSet:
    empty = []

    def __init__(self, size=100003):
        self.size = size
        self.table = [self.empty[:] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def app(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def contains(self, key):
        index = self._hash(key)
        return key in self.table[index]

hash_set = HashSet()

for num in numbers:
    hash_set.app(num)

print(sum(len(val) for val in hash_set.table))