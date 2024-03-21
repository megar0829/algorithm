N = int(input())

arr = list(map(int, input().split()))

K = int(input())

MAX_NUM = max(arr) * K + 2

dp = [1e9] * (MAX_NUM)

dp[1] = 1

for i in range(1, MAX_NUM):
    if i in arr:
        dp[i] = 1
    else:
        for j in range(1, (i // 2) + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])
    
    if dp[i] > K:
        if i % 2:
            print(f"jjaksoon win at {i}")
            
        else:
            print(f"holsoon win at {i}")
            
        break