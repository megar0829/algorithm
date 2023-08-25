import sys
input = sys.stdin.readline

L = int(input())
arr = [0] * (L + 1)
N = int(input())
max_hope = 0
hope_idx = 0
max_get = 0
get_idx = 0
for n in range(1, N + 1):
    p, k = map(int, input().split())
    if max_hope < k - p:
        max_hope = k - p
        hope_idx = n
    cnt = 0
    for i in range(p, k + 1):
        if arr[i] == 0:
            arr[i] = 1
            cnt += 1
    if max_get < cnt:
        max_get = cnt
        get_idx = n

print(hope_idx)
print(get_idx)