T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        row = 0
        max_row = 0
        for j in range(M):
            if arr[i][j] == 1:
                row += 1
            else:
                if max_row < row:
                    max_row = row
                row = 0
            if max_row < row:
                max_row = row
        if result < max_row:
            result = max_row

    for i in range(M):
        col = 0
        max_col = 0
        for j in range(N):
            if arr[j][i] == 1:
                col += 1
            else:
                if max_col < col:
                    max_col = col
                col = 0
            if max_col < col:
                max_col = col
        if result < max_col:
            result = max_col

    print(f'#{tc} {result}')