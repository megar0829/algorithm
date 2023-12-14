import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [1e9] * (k + 1)
dp [0] = 0

for coin in coins:
    for money in range(1, k + 1):
        if coin <= money:
            dp[money] = min(dp[money], dp[money - coin] + 1)
            
if dp[k] == 1e9:
    dp[k] = -1

print(dp[k])