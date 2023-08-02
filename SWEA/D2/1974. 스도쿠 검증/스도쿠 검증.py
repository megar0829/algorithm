T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = True
    for i in range(9):
        row_lst = list(range(1, 10))
        col_lst = list(range(1, 10))
        for j in range(9):
            if arr[i][j] in row_lst:
                row_lst.remove(arr[i][j])
            if arr[j][i] in col_lst:
                col_lst.remove(arr[j][i])
        if len(row_lst) or len(col_lst):
            result = False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            arr_3 = list(range(1, 10))
            for k in range(3):
                for l in range(3):
                    if arr[i + k][j + l] in arr_3:
                        arr_3.remove(arr[i + k][j + l])
            if len(arr_3):
                result = False
    if result:
        print(f'#{tc} {int(result)}')
    else:
        print(f'#{tc} {int(result)}')