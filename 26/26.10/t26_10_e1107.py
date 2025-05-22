import heapq

def prim(n, adj, banned_edge=None):
    visited = [False] * (n + 1)
    min_heap = [(0, 1, -1)]
    total_cost = 0
    count = 0
    mst_edges = []

    while min_heap and count < n:
        cost, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        count += 1
        if parent != -1:
            mst_edges.append((parent, u))

        for v, w in adj[u]:
            if not visited[v]:
                if banned_edge == (u, v) or banned_edge == (v, u):
                    continue
                heapq.heappush(min_heap, (w, v, u))

    if count == n:
        return total_cost, mst_edges
    else:
        return float('inf'), []

def read_input():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    return n, adj

def main():
    n, adj = read_input()
    cost1, edges1 = prim(n, adj)
    cost2 = float('inf')

    for edge in edges1:
        temp_cost, _ = prim(n, adj, banned_edge=edge)
        if cost1 < temp_cost < cost2:
            cost2 = temp_cost
        elif temp_cost == cost1:
            cost2 = cost1
            break

    print(f"{cost1} {cost2}")

if __name__ == "__main__":
    main()