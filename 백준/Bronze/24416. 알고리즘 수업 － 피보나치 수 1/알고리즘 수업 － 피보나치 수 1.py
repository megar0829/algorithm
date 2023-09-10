dp = [0] * 41
dp[1] = 1
dp[2] = 1
for i in range(3, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

n = int(input())
cod1 = dp[n]
cod2 = n - 2

print(cod1, cod2)