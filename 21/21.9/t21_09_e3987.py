n, m = map(int, input().split())
edges = set()

for i in range(m):
    a, b = map(int, input().split())
    edge = tuple(sorted((a, b)))
    if a != b:
        edges.add(edge)

expected = n * (n - 1) // 2

if len(edges) == expected:
    print("YES")
else:
    print("NO")
