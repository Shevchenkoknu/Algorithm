def dfs(v, graph, visited, order):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, graph, visited, order)
    order.append(v)

def reverse_dfs(v, reverse_graph, visited):
    visited[v] = True
    for u in reverse_graph[v]:
        if not visited[u]:
            reverse_dfs(u, reverse_graph, visited)

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        reverse_graph[v-1].append(u-1)

    visited = [False] * n
    order = []

    for v in range(n):
        if not visited[v]:
            dfs(v, graph, visited, order)

    visited = [False] * n
    count = 0

    for v in reversed(order):
        if not visited[v]:
            reverse_dfs(v, reverse_graph, visited)
            count += 1

    print(count)

if __name__ == "__main__":
    main()
