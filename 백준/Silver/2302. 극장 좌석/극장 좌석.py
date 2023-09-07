N = int(input())
M = int(input())
lst = [int(input()) for _ in range(M)]

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1
if M > 0:
    pre = 0
    for j in range(M):
        ans *= dp[lst[j] - 1 - pre]
        pre = lst[j]
    ans *= dp[N - pre]
else:
    ans = dp[N]
print(ans)