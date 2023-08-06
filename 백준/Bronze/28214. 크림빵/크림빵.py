N, K, P = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = 0
for i in range(N):
    save_bread = 0
    for j in range(K):
        save_bread += arr[i * K + j]
    if save_bread > K - P:
        result += 1
print(result)