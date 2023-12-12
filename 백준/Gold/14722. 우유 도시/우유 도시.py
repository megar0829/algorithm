N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        if dp[i][j] % 3 == graph[i - 1][j - 1]:
            dp[i][j] += 1
            
print(dp[N][N])