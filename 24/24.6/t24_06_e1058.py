N, M, K = map(int, input().split())
grid = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    stack = [(x, y)]
    grid[x][y] = 0
    size = 1
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                stack.append((nx, ny))
                size += 1
    return size

max_lake = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            max_lake = max(max_lake, dfs(i, j))

print(max_lake)
