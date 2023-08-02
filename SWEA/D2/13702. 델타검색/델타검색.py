T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    result = 0
    for i in range(N):
        for j in range(N):
            sum_arr = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_abs_arr = arr[i][j] - arr[ni][nj]
                    if sum_abs_arr < 0:
                        sum_abs_arr *= -1
                    sum_arr += sum_abs_arr
            result += sum_arr
    print(f'#{tc} {result}')