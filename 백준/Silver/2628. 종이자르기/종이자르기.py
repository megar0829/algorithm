import sys
input = sys.stdin.readline

M, N = map(int, input().split())
n = int(input())
row = [0, N]
col = [0, M]
for _ in range(n):
    a, b = map(int, input().split())
    if a:
        col.append(b)
    else:
        row.append(b)

row.sort()
max_row = 0
for i in range(len(row) - 1):
    save_row = row[i + 1] - row[i]
    if max_row < save_row:
        max_row = save_row


col.sort()
max_col = 0
for i in range(len(col) - 1):
    save_col = col[i + 1] - col[i]
    if max_col < save_col:
        max_col = save_col

print(max_row * max_col)