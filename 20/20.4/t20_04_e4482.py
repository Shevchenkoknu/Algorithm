import math
import sys

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a // math.gcd(a, b) * b

class SegmentTree:
    def __init__(self, data, func, neutral):
        self.n = len(data)
        self.tree = [neutral] * (4 * self.n)
        self.func = func
        self.neutral = neutral
        self._build(1, 0, self.n - 1, data)

    def _build(self, node, l, r, data):
        if l == r:
            self.tree[node] = data[l]
        else:
            m = (l + r) // 2
            self._build(node * 2, l, m, data)
            self._build(node * 2 + 1, m + 1, r, data)
            self.tree[node] = self.func(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, idx, value):
        self._update(1, 0, self.n - 1, idx, value)

    def _update(self, node, l, r, idx, value):
        if l == r:
            self.tree[node] = value
        else:
            m = (l + r) // 2
            if idx <= m:
                self._update(node * 2, l, m, idx, value)
            else:
                self._update(node * 2 + 1, m + 1, r, idx, value)
            self.tree[node] = self.func(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        if qr < l or ql > r:
            return self.neutral
        if ql <= l and r <= qr:
            return self.tree[node]
        m = (l + r) // 2
        left = self._query(node * 2, l, m, ql, qr)
        right = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self.func(left, right)

def main():
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    seg_gcd = SegmentTree(a, gcd, 0)
    seg_lcm = SegmentTree(a, lcm, 1)

    for _ in range(m):
        parts = input().split()
        q, l, r = map(int, parts)
        l -= 1
        if q == 1:
            r -= 1
            g = seg_gcd.query(l, r)
            l_ = seg_lcm.query(l, r)
            if g < l_:
                print("wins")
            elif g > l_:
                print("loser")
            else:
                print("draw")
        else:
            seg_gcd.update(l, r)
            seg_lcm.update(l, r)

if __name__ == "__main__":
    main()

