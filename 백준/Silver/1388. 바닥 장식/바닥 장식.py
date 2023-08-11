n, m = map(int, input().split())
arr = [input() for _ in range(n)]
cnt = 0
for i in range(n):
    row = 0
    cut = 0
    for j in range(m):
        if arr[i][j] == '-':
            row += 1
            cut = 0
        else:
            if row != 0 and cut == 0:
                cut += 1
                cnt += 1
                row = 0
    if cut == 0 and row != 0:
        cnt +=1

for i in range(m):
    col = 0
    cut = 0
    for j in range(n):
        if arr[j][i] == '|':
            col += 1
            cut = 0
        else:
            if col != 0 and cut == 0:
                cut += 1
                cnt += 1
                col = 0
    if cut == 0 and col != 0:
        cnt +=1
print(cnt)