n, m = map(int, input().split())

in_edge = [0] * (n + 1)
out_edge = [0] * (n + 1)

for edge in range(m):
    a, b = map(int, input().split())
    out_edge[a] += 1
    in_edge[b] += 1

for i in range(1, n + 1):
    print(in_edge[i], out_edge[i])
