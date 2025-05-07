m, n = map(int, input().split())
sheet = [input().strip() for _ in range(m)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    stack = [(x, y)]
    sheet[x] = sheet[x][:y] + '.' + sheet[x][y+1:]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and sheet[nx][ny] == '#':
                sheet[nx] = sheet[nx][:ny] + '.' + sheet[nx][ny+1:]
                stack.append((nx, ny))

count = 0

for i in range(m):
    for j in range(n):
        if sheet[i][j] == '#':
            dfs(i, j)
            count += 1

print(count)
