import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
save_val = 0
cnt = 0
for i in range(N - 1, -1, -1):
    if save_val < arr[i]:
        save_val = arr[i]
        cnt += 1
print(cnt)