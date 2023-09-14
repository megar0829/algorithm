N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr_dict = {}
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = dp[i - 1] + arr[i]

for i in range(N):
    arr_dict.setdefault(dp[i] % M, 0)
    arr_dict[dp[i] % M] += 1

if 0 in arr_dict.keys():
    result = arr_dict[0]
else:
    result = 0
    
for v in arr_dict.values():
    result += (v * (v - 1)) // 2
print(result)