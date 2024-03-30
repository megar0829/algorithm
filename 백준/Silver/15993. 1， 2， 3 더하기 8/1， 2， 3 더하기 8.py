import sys
input = sys.stdin.readline

T = int(input())

tc = [int(input()) for _ in range(T)]

L = max(tc)

dp = [[0, 0] for _ in range(L + 1)]

dp[0][0] = 1
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1

for i in range(3, L + 1):
    dp[i][0] = ((dp[i - 1][1] + dp[i - 2][1]) + dp[i - 3][1]) %  1000000009
    dp[i][1] = ((dp[i - 1][0] + dp[i - 2][0]) + dp[i - 3][0]) %  1000000009

for num in tc:
    print(dp[num][1], dp[num][0])