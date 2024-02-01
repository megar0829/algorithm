# 모듈로 연산 사용

N = int(input())

dp = [[0] * 10 for _ in range(1002)]

for i in range(10):
    dp[1][i] = 1
    
for i in range(2, 1002):
    for j in range(10):

        sum_val = 0
        for k in range(j, 10):
            sum_val += (dp[i - 1][k]) % 10007
        
        dp[i][j] = sum_val % 10007

print(dp[N + 1][0])