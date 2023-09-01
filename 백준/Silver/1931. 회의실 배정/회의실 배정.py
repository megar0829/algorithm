import sys
input = sys.stdin.readline

N = int(input())
arr = [[0, 0]]
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 0
save_val = arr[0][1]
for i in range(1, N + 1):
    if save_val <= arr[i][0]:
        cnt += 1
        save_val = arr[i][1]
print(cnt)