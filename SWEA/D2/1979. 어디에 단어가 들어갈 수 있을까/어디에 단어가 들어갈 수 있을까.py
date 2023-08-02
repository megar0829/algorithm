T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        row_lst = []
        col_lst = []
        cnt_row = 0
        cnt_col = 0
        for j in range(N):
            # 행 우선 탐색
            if arr[i][j] == 1:
                cnt_row += 1
                if j == N - 1:
                    row_lst.append(cnt_row)
            elif arr[i][j] == 0 and cnt_row != 0:
                row_lst.append(cnt_row)
                cnt_row = 0

            # 열 우선 탐색
            if arr[j][i] == 1:
                cnt_col += 1
                if j == N - 1:
                    col_lst.append(cnt_col)
            elif arr[j][i] == 0 and cnt_col != 0:
                col_lst.append(cnt_col)
                cnt_col = 0

        if K in row_lst:
            result += row_lst.count(K)
        if K in col_lst:
            result += col_lst.count(K)
    print(f'#{tc} {result}')