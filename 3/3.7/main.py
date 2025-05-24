import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    x = 0
    n = int(data[x])
    x += 1
    colors = list(map(int, data[x:x + n]))
    x += n
    m = int(data[x])
    x += 1
    queries = list(map(int, data[x:x + m]))
    results = []

    for q in queries:
        left = bisect.bisect_left(colors, q)
        right = bisect.bisect_right(colors, q)
        results.append(str(right - left))
    print('\n'.join(results))

main()
