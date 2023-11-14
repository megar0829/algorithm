text1 = input()
text2 = input()

N = len(text1)
M = len(text2)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if text1[i - 1] == text2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

result = 0
for i in range(1, N + 1):
    result = max(result, max(dp[i]))

print(result)
