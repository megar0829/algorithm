import sys
input = sys.stdin.readline


T, W = map(int, input().split())

tree_num = [0] + [int(input()) for _ in range(T)]

dp = [[0] * (W + 1) for _ in range(T + 1)]

for t in range(1, T + 1):
    if tree_num[t] == 1:
        dp[t][0] = dp[t - 1][0] + 1
    else:
        dp[t][0] = dp[t - 1][0]

    for w in range(1, W + 1):
        if (tree_num[t] == 1 and not w % 2) or (tree_num[t] == 2 and w % 2):
            dp[t][w] = max(dp[t - 1][w], dp[t - 1][w - 1]) + 1
        else:
            dp[t][w] = max(dp[t - 1][w], dp[t - 1][w - 1])

print(max(dp[T]))