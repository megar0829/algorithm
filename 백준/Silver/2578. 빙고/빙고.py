def bingo(input_arr, n):
    global cnt
    stop_point = 0
    for i in range(5):
        for j in range(5):
            if input_arr[i][j] == n:
                input_arr[i][j] = -1
                cnt += 1
                stop_point += 1
                break
        if stop_point == 1:
            break

    if cnt >= 12:
        # 행 우선 탐색
        # 열 우선 탐색
        # 대각선 우선 탐색
        bingo_cnt = 0
        dig_sum1 = 0
        dig_sum2 = 0
        for i in range(5):
            row_sum = 0
            col_sum = 0
            dig_sum1 += input_arr[i][i]
            dig_sum2 += input_arr[i][4 - i]
            for j in range(5):
                row_sum += input_arr[i][j]
                col_sum += input_arr[j][i]
            if row_sum == -5:
                bingo_cnt += 1
            if col_sum == -5:
                bingo_cnt += 1
        if dig_sum1 == -5:
            bingo_cnt += 1
        if dig_sum2 == -5:
            bingo_cnt += 1
        if bingo_cnt >= 3:
            return False
    return input_arr


arr = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
result = 0
for _ in range(5):
    numbers = list(map(int, input().split()))
    if result == 0:
        for k in range(5):
            arr = bingo(arr, numbers[k])
            if arr is False:
                result = cnt
                break
print(result)