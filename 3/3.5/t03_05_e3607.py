import sys
import bisect

for line in sys.stdin:
    n = int(line)
    heights = list(map(int, sys.stdin.readline().split()))
    a, b = map(int, sys.stdin.readline().split())

    heights.sort()
    left = bisect.bisect_left(heights, a)
    right = bisect.bisect_right(heights, b)

    print(right - left)
