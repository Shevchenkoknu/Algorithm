import heapq

def case(visitors):
    visitors.sort()
    total_negative = 0
    queue = []
    time = 0
    idx = 0
    n = len(visitors)

    while idx < n or queue:
        while idx < n and visitors[idx][0] <= time:
            heapq.heappush(queue, (-visitors[idx][1], visitors[idx][0]))
            idx += 1

        if queue:
            w, r = heapq.heappop(queue)
            w = -w
            total_negative += w * (time - r)
            time += 1
        else:
            if idx < n:
                time = visitors[idx][0]

    return total_negative


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        visitors = []
        for _ in range(n):
            r, w = map(int, input().split())
            visitors.append((r, w))

        result = case(visitors)
        print(result)

if __name__ == "__main__":
    main()
