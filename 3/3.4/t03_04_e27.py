def linear(heights, a, b):
    count = 0
    for h in heights:
        if a <= h <= b:
            count += 1
    return count

n = int(input())
heights = list(map(int, input().split()))
a, b = map(int, input().split())

print(count_linear(heights, a, b))
