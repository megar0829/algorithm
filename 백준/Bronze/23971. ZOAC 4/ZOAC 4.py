import sys
input = sys.stdin.readline

H, W, N, M = list(map(int, input().split()))
row = 0
col = 0
for i in range(0, H, N + 1):
    row += 1
for j in range(0, W, M + 1):
    col += 1

print(row * col)