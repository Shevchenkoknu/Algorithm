from collections import defaultdict
import sys

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def connected(n, edges, to_remove):
    graph = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        if i not in to_remove:
            graph[u].append(v)
            graph[v].append(u)
    visited = [False] * (n + 1)
    dfs(1, visited, graph)
    return all(visited[1:])

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1

    edges = []
    for _ in range(M):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))

    K = int(data[idx]); idx += 1

    results = []
    for _ in range(K):
        C = int(data[idx]); idx += 1
        to_remove = set(int(data[idx + i]) - 1 for i in range(C))
        idx += C
        if connected(N, edges, to_remove):
            results.append("Connected")
        else:
            results.append("Disconnected")

    print("\n".join(results))

if __name__ == "__main__":
    main()