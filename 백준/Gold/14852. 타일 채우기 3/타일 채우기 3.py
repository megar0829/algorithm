dp = [0] * (1000001)
dp[0] = 1
dp[1] = 2
dp[2] = 7

for i in range(3, 1000001):
    dp[i] = (dp[i - 1] * 3 + dp[i - 2] - dp[i - 3]) % 1000000007

n = int(input())
print(dp[n])