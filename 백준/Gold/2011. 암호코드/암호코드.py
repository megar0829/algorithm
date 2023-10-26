code = [0] + list(map(int, input()))
n = len(code)

dp = [0] * (n)
dp[0] = 1

if code[1] == '0':
    print(0)
else:
    for i in range(1, n):
        if code[i] > 0:
            dp[i] += dp[i - 1]

        if (code[i] <= 6 and code[i - 1] == 2) or (code[i - 1] == 1):
            if i > 1:
                dp[i] += dp[i - 2]

    dp[i] %= 1000000

print(dp[n - 1])