import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
        else:
            m = (l + r) // 2
            self.build(data, node * 2, l, m)
            self.build(data, node * 2 + 1, m + 1, r)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
        else:
            m = (l + r) // 2
            if idx <= m:
                self.update(node * 2, l, m, idx, val)
            else:
                self.update(node * 2 + 1, m + 1, r, idx, val)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        m = (l + r) // 2
        left = self.query(node * 2, l, m, ql, qr)
        right = self.query(node * 2 + 1, m + 1, r, ql, qr)
        return left + right

    def get_sum(self, r):
        if r < 0:
            return 0
        return self.query(1, 0, self.n - 1, 0, r)

    def set_value(self, idx, val):
        self.update(1, 0, self.n - 1, idx, val)

n = int(input())
A = list(map(int, input().split()))
m = int(input())

seg = SegmentTree(A)
output = []

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        v = query[1]
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if seg.get_sum(mid) <= v:
                lo = mid + 1
            else:
                hi = mid
        output.append(str(lo))

    else:
        x, y = query[1], query[2]
        seg.set_value(x - 1, y)

print('\n'.join(output))