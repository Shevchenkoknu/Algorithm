import sys
input = sys.stdin.read

class Node:
    def __init__(self, val=None):
        self.left_value = val
        self.right_value = val
        self.prefix_len = 1
        self.suffix_len = 1
        self.max_len = 1
        self.length = 1
        self.lazy = None

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [None] * (4 * self.n)
        self.lazy = [None] * (4 * self.n)
        self.build(data, 1, 0, self.n - 1)

    def make_node(self, val):
        node = Node(val)
        return node

    def build(self, data, node, l, r):
        if l == r:
            self.tree[node] = self.make_node(data[l])
        else:
            m = (l + r) // 2
            self.build(data, node * 2, l, m)
            self.build(data, node * 2 + 1, m + 1, r)
            self.tree[node] = self.merge(self.tree[node * 2], self.tree[node * 2 + 1])

    def merge(self, left, right):
        node = Node()
        node.left_value = left.left_value
        node.right_value = right.right_value
        node.length = left.length + right.length

        node.prefix_len = left.prefix_len
        if left.prefix_len == left.length and left.right_value <= right.left_value:
            node.prefix_len += right.prefix_len

        node.suffix_len = right.suffix_len
        if right.suffix_len == right.length and left.right_value <= right.left_value:
            node.suffix_len += left.suffix_len

        node.max_len = max(left.max_len, right.max_len)
        if left.right_value <= right.left_value:
            node.max_len = max(node.max_len, left.suffix_len + right.prefix_len)

        return node

    def push(self, node, l, r):
        if self.lazy[node] is not None:
            v = self.lazy[node]
            self.tree[node] = Node(v)
            self.tree[node].length = r - l + 1
            self.tree[node].prefix_len = self.tree[node].suffix_len = self.tree[node].max_len = r - l + 1
            self.tree[node].left_value = self.tree[node].right_value = v
            if l != r:
                self.lazy[node * 2] = v
                self.lazy[node * 2 + 1] = v
            self.lazy[node] = None

    def update(self, node, l, r, ul, ur, val):
        self.push(node, l, r)
        if ur < l or r < ul:
            return
        if ul <= l and r <= ur:
            self.lazy[node] = val
            self.push(node, l, r)
            return
        m = (l + r) // 2
        self.update(node * 2, l, m, ul, ur, val)
        self.update(node * 2 + 1, m + 1, r, ul, ur, val)
        self.tree[node] = self.merge(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, node, l, r, ql, qr):
        self.push(node, l, r)
        if qr < l or r < ql:
            return None
        if ql <= l and r <= qr:
            return self.tree[node]
        m = (l + r) // 2
        left = self.query(node * 2, l, m, ql, qr)
        right = self.query(node * 2 + 1, m + 1, r, ql, qr)
        if left is None:
            return right
        if right is None:
            return left
        return self.merge(left, right)

lines = list(map(int, input().split()))
N = lines[0]
data = lines[1:N+1]
M = lines[N+1]

tree = SegmentTree(data)
output = []

i = N + 2
while i < len(lines):
    query_type = lines[i]
    if query_type == 1:
        l = lines[i + 1]
        r = lines[i + 2]
        res = tree.query(1, 0, N - 1, l - 1, r - 1)
        output.append(str(res.max_len))
        i += 3
    elif query_type == 2:
        l = lines[i + 1]
        r = lines[i + 2]
        v = lines[i + 3]
        tree.update(1, 0, N - 1, l - 1, r - 1, v)
        i += 4

print('\n'.join(output))