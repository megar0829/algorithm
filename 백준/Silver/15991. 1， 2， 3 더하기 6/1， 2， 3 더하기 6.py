dp = [0] * (100001)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3

for num in range(6, 100001):
    dp[num] = (dp[num - 2] + dp[num - 4] + dp[num - 6]) % 1000000009

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])