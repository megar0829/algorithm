def row(i, j, k):
    cnt = 0
    for n in range(0, i + 1):
        for m in range(M):
            if arr[n][m] != 'W':
                cnt += 1
    
    for n in range(i + 1, j + 1):
        for m in range(M):
            if arr[n][m] != 'B':
                cnt += 1
    
    for n in range(j + 1, N):
        for m in range(M):
            if arr[n][m] != 'R':
                cnt += 1
    return cnt
        

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_row = N * M
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                save_row = row(i, j, k)
                if min_row > save_row:
                    min_row = save_row

    print(f'#{tc} {min_row}')