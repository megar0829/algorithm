def dfs(n):
    dp.setdefault(n, 0)

    if dp[n]:
        return dp[n]

    dp[n] = dfs(n // P) + dfs(n // Q)
    return dp[n]


N, P, Q = map(int, input().split())

dp = {}
dp[0] = 1

print(dfs(N))