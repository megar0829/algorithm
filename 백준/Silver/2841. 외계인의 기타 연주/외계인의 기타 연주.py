import sys
input = sys.stdin.readline

N, P = map(int, input().split())
arr = [[] for _ in range(N + 1)]
cnt = 0
for _ in range(N):
    n, p = map(int, input().split())
    if not arr[n] or arr[n][-1] < p:
        arr[n].append(p)
        cnt += 1
    elif arr[n][-1] == p:
        continue
    else:
        while arr[n] and arr[n][-1] > p:
            arr[n].pop()
            cnt += 1
        if arr[n] and arr[n][-1] == p:
            continue
        else:
            arr[n].append(p)
            cnt += 1
    
print(cnt)