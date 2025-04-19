from math import gcd, log2, ceil

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        p = ceil(log2(k))
        self.n = n = 2 ** p
        self._items = [0] * (2 * n)
        for i in range(k):
            self._items[n + i] = array[i]
        for i in range(n - 1, 0, -1):
            self._items[i] = gcd(self._items[2 * i], self._items[2 * i + 1])

    def query(self, a, b):
        left = a + self.n
        right = b + self.n
        res = 0
        while left <= right:
            if left % 2 == 1:
                res = gcd(res, self._items[left])
                left += 1
            if right % 2 == 0:
                res = gcd(res, self._items[right])
                right -= 1
            left //= 2
            right //= 2
        return res

    def update(self, i, item):
        i = self.n + i
        self._items[i] = item
        i //= 2
        while i > 0:
            self._items[i] = gcd(self._items[2 * i], self._items[2 * i + 1])
            i //= 2


if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))
        m = int(f.readline().strip())
        tree = SegmentTree(arr)

        for _ in range(m):
            line = f.readline().strip()
            if not line:
                continue
            c, l, r = map(int, line.split())
            if c == 1:
                print(tree.query(l - 1, r - 1))
            elif c == 2:
                tree.update(l - 1, r)
