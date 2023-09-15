import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key=lambda x:(x[1], x[0]))

cnt = 0
save_val = 0
for i in range(N):
    if arr[i][0] >= save_val:
        save_val = arr[i][1]
        cnt += 1
print(cnt)