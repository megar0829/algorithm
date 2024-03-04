N = int(input())
arr = input()

dp = [1e9] * N

dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if (arr[i] == 'O' and arr[j] == 'B') \
            or (arr[i] == 'J' and arr[j] == 'O') \
                or (arr[i] == 'B' and arr[j] == 'J'):
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

if dp[N - 1] == 1e9:
    dp[N - 1] = -1
    
print(dp[N - 1])