import sys
input = sys.stdin.readline


N = int(input())

dp = [[(0, 0), (0, 0)] for _ in range(N + 1)]

arr = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(1, min(arr[0][0], arr[0][1]))

else:
    dp[0] = [(arr[0][0], 1), (arr[0][1], 1)]
    
    for i in range(1, N):
        A, B = arr[i]
        
        if A == dp[i - 1][0][0]:
            dp[i][0] = (A, dp[i - 1][0][1] + 1)
            
        elif A == dp[i - 1][1][0]:
            dp[i][0] = (A, dp[i - 1][1][1] + 1)
            
        else:
            dp[i][0] = (A, 1)
            
        
        if B == dp[i - 1][0][0]:
            dp[i][1] = (B, dp[i - 1][0][1] + 1)
            
        elif B == dp[i - 1][1][0]:
            dp[i][1] = (B, dp[i - 1][1][1] + 1)
            
        else:
            dp[i][1] = (B, 1)
        
    max_cnt, max_val = 0, 0

    for i in range(N):
        if dp[i][0][1] > max_cnt:
            max_cnt = dp[i][0][1]
            max_val = dp[i][0][0]
        elif dp[i][0][1] == max_cnt:
            max_val = min(max_val, dp[i][0][0])
            
        if dp[i][1][1] > max_cnt:
            max_cnt = dp[i][1][1]
            max_val = dp[i][1][0]
        elif dp[i][1][1] == max_cnt:
            max_val = min(max_val, dp[i][1][0])
            
    print(max_cnt, max_val)