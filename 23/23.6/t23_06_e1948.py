from collections import deque


def topological_sort(n, edges):
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != n:
        return [-1]

    return topo_order


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    edges = []

    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    result = topological_sort(n, edges)
    print(' '.join(map(str, result)))
