import heapq

INF = float('inf')
n, m = map(int, input().split())
s, f = map(int, input().split())

def dijkstra(n, graph, start, end):
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))
    if dist[end] == INF:
        return -1, []

    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return dist[end], path

graph = [[] for _ in range(n + 1)]
u, v, w = map(int, input().split())

for _ in range(m):
    graph[u].append((v, w))
    graph[v].append((u, w))

distance, path = dijkstra(n, graph, s, f)

if distance == -1:
    print(-1)
else:
    print(distance)
    print(' '.join(map(str, path)))
