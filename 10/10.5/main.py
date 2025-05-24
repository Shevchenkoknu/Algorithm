import sys

def solve(N: int, tracks: list[int]):
    dp = [0] * (N + 1)
    for track in tracks:
        for i in range(N, track - 1, -1):
            dp[i] = max(dp[i], dp[i - track] + track)
    print(f"sum:{dp[N]}")

if __name__ == "__main__":
    for line in sys.stdin:
        data = list(map(int, line.split()))
        N, count, tracks = data[0], data[1], data[2:]
        solve(N, tracks)