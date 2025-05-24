import sys
input = sys.stdin.read

def cows(stalls, k, min_dist):
    count = 1
    last_pos = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= min_dist:
            count += 1
            last_pos = stalls[i]
            if count == k:
                return True
    return False

def distance(stalls, k):
    left = 0
    right = stalls[-1] - stalls[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if cows(stalls, k, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

def main():
    data = input().split()
    n, k = int(data[0]), int(data[1])
    stalls = list(map(int, data[2:2 + n]))
    print(distance(stalls, k))

if __name__ == "__main__":
    main()
