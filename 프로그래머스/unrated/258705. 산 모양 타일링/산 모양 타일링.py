def solution(n, tops):
    dp = [[0] * 2 for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(n):
        if tops[i]:
            dp[i + 1][0] = (dp[i][0] * 3 + dp[i][1] * 2) % 10007
        else:
            dp[i + 1][0] = (dp[i][0] * 2 + dp[i][1] * 1) % 10007

        dp[i + 1][1] = (dp[i][0] + dp[i][1]) % 10007
    
    answer = (dp[n][0] + dp[n][1]) % 10007
    return answer