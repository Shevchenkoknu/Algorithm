import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    x = 0
    n = int(data[x])
    x += 1
    collection = list(map(int, data[x:x + n]))
    x += n
    m = int(data[x])
    x += 1
    queries = list(map(int, data[x:x + m]))
    results = []

    for k in queries:
        i = bisect.bisect_left(collection, k)
        if i < n and collection[i] == k:
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))\

main()
