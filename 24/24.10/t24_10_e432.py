from collections import deque
import sys

input = sys.stdin.read
data = input().split('\n')
idx = 0

while idx < len(data):
    if not data[idx].strip():
        idx += 1
        continue
    LRC = data[idx].strip()
    if LRC == '0 0 0':
        break
    L, R, C = map(int, LRC.split())
    idx += 1

    maze = []
    start = None
    for l in range(L):
        level = []
        for r in range(R):
            line = data[idx].strip()
            for c in range(C):
                if line[c] == 'S':
                    start = (l, r, c)
            level.append(list(line))
            idx += 1
        maze.append(level)
        idx += 1

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    queue = deque()
    queue.append((start[0], start[1], start[2], 0))
    visited[start[0]][start[1]][start[2]] = True

    directions = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]

    escaped = False

    while queue:
        z, x, y, minutes = queue.popleft()
        if maze[z][x][y] == 'E':
            print(f"Escaped in {minutes} minute(s).")
            escaped = True
            break
        for dz, dx, dy in directions:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[nz][nx][ny] and maze[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    queue.append((nz, nx, ny, minutes + 1))
    if not escaped:
        print("Trapped!")
