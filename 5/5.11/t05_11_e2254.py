import sys
input = sys.stdin.read

def possible(x, k, B):
    prefix_sum = [0] * (len(x) + 1)
    for i in range(len(x)):
        prefix_sum[i + 1] = prefix_sum[i] + x[i]
    min_cost = float('inf')

    for i in range(len(x) - k + 1):
        j = i + k - 1
        mid = (i + j) // 2
        median = x[mid]
        left = median * (mid - i) - (prefix_sum[mid] - prefix_sum[i])
        right = (prefix_sum[j + 1] - prefix_sum[mid + 1]) - median * (j - mid)
        total_cost = left + right

        if total_cost <= B:
            return True
    return False

def max(x, L, B):
    R = len(x)
    low, high = 0, R
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if possible(x, mid, B):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

def main():
    data = input().split()
    R = int(data[0])
    L = int(data[1])
    B = int(data[2])
    x = list(map(int, data[3:]))
    print(max(x, L, B))

if __name__ == "__main__":
    main()
