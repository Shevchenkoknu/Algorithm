import sys
import math
import heapq

def prim(points):
    n = len(points)
    visited = [False] * n
    min = [float('inf')] * n
    min[0] = 0
    pq = [(0, 0)]
    total = 0.0

    while pq:
        weight, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total += weight

        for v in range(n):
            if not visited[v]:
                dist = math.hypot(points[u][0] - points[v][0], points[u][1] - points[v][1])
                if dist < min[v]:
                    min[v] = dist
                    heapq.heappush(pq, (dist, v))

    return total

def main():
    input_lines = sys.stdin.read().splitlines()
    i = 0
    while i < len(input_lines):
        n = int(input_lines[i])
        if n == 0:
            break
        i += 1
        points = []
        for _ in range(n):
            x, y = map(int, input_lines[i].split())
            points.append((x, y))
            i += 1
        result = prim(points)
        print(f"{result:.2f}")

if __name__ == "__main__":
    main()
