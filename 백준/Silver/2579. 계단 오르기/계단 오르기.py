import sys
input = sys.stdin.readline


N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(arr[1])
else:
    dp = [0] * (N + 1)

    dp[1] = arr[1]
    dp[2] = dp[1] + arr[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + arr[i - 1]) + arr[i]
    print(dp[N])