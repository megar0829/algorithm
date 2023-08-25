def delta(i, j):
    save_val = arr[i][j]
    for m in range(1, M):
        for k in range(4):
            ni = i + di[k] * m
            nj = j + dj[k] * m
            if 0 <= ni < N and 0 <= nj < N:
                save_val += arr[ni][nj]
    return save_val


def delta_s(i, j):
    save_val = arr[i][j]
    for m in range(1, M):
        for k in range(4):
            ni = i + dsi[k] * m
            nj = j + dsj[k] * m
            if 0 <= ni < N and 0 <= nj < N:
                save_val += arr[ni][nj]
    return save_val


T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dsi = [-1, 1, 1, -1]
dsj = [1, 1, -1, -1]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            save_delta = max(delta(i, j), delta_s(i, j))
            if result < save_delta:
                result = save_delta

    print(f'#{tc} {result}')