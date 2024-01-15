dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

dp[3] = 2
# dp[4] = 4

# dp[5] = 4
# dp[6] = 6

# dp[7] = 6
# dp[8] = 10

# dp[9] = 10
# dp[10] = 14

for i in range(4, 1000001):
    if i % 2:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 1] + dp[i // 2]) % 1000000000


N = int(input())

print(dp[N])