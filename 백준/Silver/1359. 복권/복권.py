from itertools import combinations

N, M, K = map(int, input().split())

arr = [*combinations([i for i in range(N)], M)]

result = 0

for lst in arr:
    cnt = 0 
    
    for idx in range(M):
        if lst[idx] < M:
            cnt += 1
    
    if cnt >= K:
        result += 1

print(result / len(arr))