import sys

data = list(map(int, sys.stdin.read().split()))
index = 0
edges = []

n = data[index]; index += 1
d = data[index]; index += 1
v = data[index]; index += 1
r = data[index]; index += 1

for _ in range(r):
    u = data[index]; index += 1
    t1 = data[index]; index += 1
    to = data[index]; index += 1
    t2 = data[index]; index += 1
    edges.append((u, t1, to, t2))

INF = float('inf')
dist = [INF] * (n + 1)
dist[d] = 0

for _ in range(n - 1):
    updated = False
    for u, t1, to, t2 in edges:
        if dist[u] <= t1 and dist[to] > t2:
            dist[to] = t2
            updated = True
    if not updated:
        break

print(dist[v] if dist[v] != INF else -1)