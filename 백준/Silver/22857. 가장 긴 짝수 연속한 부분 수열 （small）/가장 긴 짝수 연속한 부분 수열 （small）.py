N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt, start, end, arr_len, max_len = 0, 0, 0, 0, 0
flag = True

for start in range(N):
    while cnt <= K and flag:
        if arr[end] % 2:
            if cnt == K:
                break
            cnt += 1
        arr_len += 1
        if end == N - 1:
            flag = False
            break
        end += 1
        
    max_len = max(max_len, arr_len - cnt)
        
    if arr[start] % 2:
        cnt -= 1
        
    arr_len -= 1

print(max_len)