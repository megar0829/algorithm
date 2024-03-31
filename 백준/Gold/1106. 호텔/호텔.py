import sys
input = sys.stdin.readline

C, N = map(int, input().split())

dp = [1e9] * (C + 100)

dp[0] = 0

for _ in range(N):
    cost, customer = map(int, input().split())
    
    for i in range(customer, C + 100):
        dp[i] = min(dp[i - customer] + cost, dp[i])

print(min(dp[C:]))