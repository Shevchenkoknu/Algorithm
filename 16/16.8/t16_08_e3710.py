import sys

MODULO = 1000000007
Q = 127
n = int(sys.stdin.readline().strip())

def mod_exp(base, exp, mod):
    result = 1
    while exp:
        if exp % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def dfs(node, tree, values):
    subtree_values = []

    for child in tree[node]:
        child_values = dfs(child, tree, values)
        subtree_values.extend(child_values)

    subtree_values.append(values[node])

    if len(subtree_values) > 1:
        subtree_values.sort()
        min_diff = min(
            abs(subtree_values[i] - subtree_values[i - 1])
            for i in range(1, len(subtree_values)))
        results[node] = min_diff

    return subtree_values

tree = [[] for _ in range(n)]
values = [0] * n
parent = [-1] * n
results = [0] * n
root = -1

for i in range(n):
    p, v = map(int, sys.stdin.readline().split())
    values[i] = v
    parent[i] = p
    if p != -1:
        tree[p].append(i)
    else:
        root = i

dfs(root, tree, values)
final_sum = sum((results[i] * mod_exp(Q, i, MODULO)) % MODULO for i in range(n) if results[i] > 0) % MODULO
print(final_sum)
