N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(N):
    dp[i + 1] = dp[i]
    min_val = arr[i]
    max_val = arr[i]
    j = i - 1
    for j in range(i - 1, -1, -1):
        if arr[j] < min_val or arr[j] > max_val:
            min_val, max_val = min(arr[j], min_val), max(arr[j], max_val)
            dp[i + 1] = max(dp[i + 1], dp[j] + max_val - min_val)
            j -= 1
        else:
            break
        
print(dp[N])