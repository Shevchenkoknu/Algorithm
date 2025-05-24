import sys

def sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = sort(array[:mid])
    right = sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    robots = []
    index = 1

    for _ in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        robots.append((a, b))
        index += 2

    sorted_robots = sort(robots)

    for robot in sorted_robots:
        print(robot[0], robot[1])

if __name__ == "__main__":
    main()