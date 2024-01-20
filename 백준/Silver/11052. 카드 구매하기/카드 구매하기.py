N = int(input())
card = list(map(int, input().split()))

dp = [0] + card[:]

for i in range(1, N + 1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i - j] + card[j - 1])

print(dp[N])