N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열 생성
dp = [0] * (N + 1)

for i in range(K):
    dp[K] += arr[i]

for i in range(K, N):
    dp[i + 1] = dp[i] - arr[i - K] + arr[i]

print(max(dp[K:]))