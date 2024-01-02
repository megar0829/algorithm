N = int(input())

dp = [1e9] * (N + 1)
dp[0] = 0

for coin in range(1, N + 1):
    dp[coin] = dp[coin - 1] + 1
    
    if coin >= 2:
        dp[coin] = min(dp[coin], dp[coin - 2] + 1)
        
    if coin >= 5:
        dp[coin] = min(dp[coin], dp[coin - 5] + 1)
        
    if coin >= 7:
        dp[coin] = min(dp[coin], dp[coin - 7] + 1)
    
print(dp[N])