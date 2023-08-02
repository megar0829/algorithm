T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    for i in range(N):
        for j in range(M):
            sum_flower = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    sum_flower += arr[ni][nj]
            if result < sum_flower:
                result = sum_flower
    print(f'#{tc} {result}')