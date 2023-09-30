import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
arr = [1] * (N + 1)
for _ in range(B):
    arr[int(input())] = 0

cnt = 0
for i in range(1, K + 1):
    if not arr[i]:
        cnt += 1

min_cnt = 1e9
for i in range(K + 1, N + 1):
    if not arr[i]:
        cnt += 1
    if not arr[i - K]:
        cnt -= 1
    min_cnt = min(min_cnt, cnt)
print(min_cnt)