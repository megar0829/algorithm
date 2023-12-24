R, C, W = map(int, input().split())

dp = [[0] * i for i in range(1, 31)]

dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, 30):
    for j in range(i + 1):
        if j == i:
            dp[i][j] = 1
        
        elif j == 0:
            dp[i][j] = 1
        
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
ans = 0
for i in range(W):
    for j in range(i + 1):
        ans += dp[(R - 1) + i][(C - 1) + j]

print(ans)