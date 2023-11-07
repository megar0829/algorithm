text1 = input()
text2 = input()

n = len(text1)
m = len(text2)

dp = [[[0, ''] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if text1[i - 1] == text2[j - 1]:
            dp[i][j][0] = dp[i - 1][j - 1][0] + 1
            dp[i][j][1] = dp[i - 1][j - 1][1] + text1[i - 1]
        else:
            if dp[i - 1][j][0] >= dp[i][j - 1][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

for rlt in dp[n][m]:
    print(rlt)