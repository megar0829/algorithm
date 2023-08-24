N, K = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0
for i in range(K):
    max_sum += arr[i]
    
save_sum = max_sum
for i in range(K, N):
    save_sum += arr[i] - arr[i - K]
    if max_sum < save_sum:
        max_sum = save_sum

print(max_sum)