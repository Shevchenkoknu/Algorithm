from collections import deque

def operations(num_str):
    results = []
    digits = list(num_str)

    if digits[0] != '9':
        new_digits = digits[:]
        new_digits[0] = str(int(new_digits[0]) + 1)
        results.append(''.join(new_digits))

    if digits[3] != '1':
        new_digits = digits[:]
        new_digits[3] = str(int(new_digits[3]) - 1)
        results.append(''.join(new_digits))

    results.append(digits[3] + digits[0] + digits[1] + digits[2])
    results.append(digits[1] + digits[2] + digits[3] + digits[0])

    return [n for n in results if '0' not in n]

def bfs(start, goal):
    visited = set()
    prev = dict()

    queue = deque()
    queue.append(start)
    visited.add(start)
    prev[start] = None

    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in operations(current):
            if neighbor not in visited:
                visited.add(neighbor)
                prev[neighbor] = current
                queue.append(neighbor)

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    return path

start = input().strip()
goal = input().strip()

result_path = bfs(start, goal)
for number in result_path:
    print(number)
