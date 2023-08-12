import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 1001
max_val = 0
max_idx = 0
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    if max_val < H:
        max_val = H
        max_idx = L
        
save_p = 0
save_idx = 0
check = 0
turn_point = 0
cnt = 0
result = max_val
for i in range(1, max_idx):
    if arr[i] != 0:
        if save_p < arr[i]:
            result += (i - save_idx) * save_p
            save_p = arr[i]
            save_idx = i
result += (max_idx - save_idx) * save_p
save_p = 0

for i in range(1000, max_idx, -1):
    if arr[i] != 0:  
        if save_p < arr[i]:
            result += (save_idx - i) * save_p
            save_p = arr[i]
            save_idx = i
result += (save_idx - max_idx) * save_p
print(result)