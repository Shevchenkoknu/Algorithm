n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

def insertion_sort(times):
    n = len(times)
    for i in range(1, n):
        key = times[i]
        j = i - 1
        while j >= 0 and (
            (key[0] < times[j][0]) or
            (key[0] == times[j][0] and key[1] < times[j][1]) or
            (key[0] == times[j][0] and key[1] == times[j][1] and key[2] < times[j][2])):
            times[j + 1] = times[j]
            j -= 1
        times[j + 1] = key
insertion_sort(times)

for t in times:
    print(*t)
