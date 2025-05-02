import sys
sys.setrecursionlimit(200000)

def dfs(v, graph, visited, component):
    visited[v] = True
    component.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, component)

def find_components(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    components = []

    for v in range(1, n + 1):
        if not visited[v]:
            component = []
            dfs(v, graph, visited, component)
            components.append(component)

    return components

if __name__ == "__main__":
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

    components = find_components(n, edges)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(" ".join(map(str, comp)))