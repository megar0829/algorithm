N, M = map(int, input().split())
castle = [list(input()) for _ in range(N)]
cnt_a = 0
for i in range(N):
    dot = 0
    for j in range(M):
        if castle[i][j] == 'X':
            dot += 1
    if dot == 0:
        cnt_a += 1
cnt_b = 0
for i in range(M):
    dot = 0
    for j in range(N):
        if castle[j][i] == 'X':
            dot += 1
    if dot == 0:
        cnt_b += 1
if cnt_a > cnt_b:
    print(cnt_a)
else:
    print(cnt_b)