import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * N

meeting = [list(map(int, input().split())) for _ in range(N)]

meeting.sort()

dp[0] = meeting[0][2]

for i in range(1, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + meeting[i][2])

print(dp[N - 1])