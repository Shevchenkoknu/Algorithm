from collections import deque, defaultdict

def fire(n, m, edges, k, starts):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    time = [-1] * (n + 1)
    q = deque()

    for s in starts:
        time[s] = 0
        q.append(s)

    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if time[neighbor] == -1:
                time[neighbor] = time[current] + 1
                q.append(neighbor)

    max_time = -1
    min_vertex = -1
    for i in range(1, n + 1):
        if time[i] > max_time:
            max_time = time[i]
            min_vertex = i
        elif time[i] == max_time and i < min_vertex:
            min_vertex = i

    return max_time, min_vertex

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
starts = list(map(int, input().split()))

t, v = fire(n, m, edges, k, starts)
print(t)
print(v)
