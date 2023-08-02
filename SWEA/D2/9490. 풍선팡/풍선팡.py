T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    result = 0
    for i in range(N):
        for j in range(M):
            sum_flower = arr[i][j]
            flower = arr[i][j]
            for k in range(1, flower + 1):
                for l in range(4):
                    ni = i + di[l] * k
                    nj = j + dj[l] * k
                    if 0 <= ni < N and 0 <= nj < M:
                        sum_flower += arr[ni][nj]
            if result < sum_flower:
                result = sum_flower
    print(f'#{tc} {result}')