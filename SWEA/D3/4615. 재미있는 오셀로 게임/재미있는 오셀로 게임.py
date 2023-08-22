def othello(row, col, color):
    if color == 1:
        color = 'B'
    else:
        color = 'W'
    arr[row][col] = color
    for k in range(8):
        ni, nj = row + di[k], col + dj[k]
        if 0 <= ni < N + 1 and 0 <= nj < N + 1:
            if arr[ni][nj] == bw[color]:
                mi, mj = ni, nj
                cnt = 1
                check = False
                while True:
                    mi += di[k]
                    mj += dj[k]
                    if mi < 0 or mi >= N + 1 or mj < 0 or mj >= N + 1:
                        break
                    if arr[mi][mj] == 0:
                        break
                    if arr[mi][mj] == bw[color]:
                        cnt += 1
                    elif arr[mi][mj] == color:
                        check = True
                        break
                if check:
                    for l in range(1, cnt + 1):
                        if 0 <= ni < N + 1 and 0 <= nj < N + 1:
                            arr[ni][nj] = color
                            ni += di[k]
                            nj += dj[k]


T = int(input())
bw = {'B': 'W', 'W': 'B'}
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    arr[N // 2][N // 2] ='W'
    arr[N // 2 + 1][N // 2 + 1] ='W'
    arr[N // 2][N // 2 + 1] ='B'
    arr[N // 2 + 1][N // 2] ='B'
    for _ in range(M):
        othello(*list(map(int, input().split())))

    B = W = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == 'B':
                B += 1
            elif arr[i][j] == 'W':
                W += 1
    print(f'#{tc} {B} {W}')