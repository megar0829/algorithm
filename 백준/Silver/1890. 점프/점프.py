import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if (i, j) == (N - 1, N - 1):
            break
            
        if dp[i][j]:
            jump = arr[i][j]
            if 0 <= i + jump < N:
                dp[i + jump][j] += dp[i][j]

            if 0 <= j + jump < N:
                dp[i][j + jump] += dp[i][j]


print(dp[N - 1][N - 1])