n = int(input())
count = 0

for i in range(n):
    matrix = list(map(int, input().split()))
    if sum(matrix) == 1:
        count += 1

print(count)
