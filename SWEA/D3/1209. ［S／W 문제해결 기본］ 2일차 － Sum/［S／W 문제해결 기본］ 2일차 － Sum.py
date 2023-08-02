for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_dig = 0
            sum_row += arr[i][j]
            sum_col += arr[j][i]
            if i == 0 or j == 0:
                sum_dig += arr[i][j]
                ni = i + 1
                nj = j + 1
                for k in range(i, 101):
                    if ni >= 100 or nj >= 100:
                        break
                    sum_dig += arr[ni][nj]
                    ni += 1
                    nj += 1

        if result < sum_row:
            result = sum_row
        if result < sum_col:
            result = sum_col
        if result < sum_dig:
            result = sum_dig

    print(f'#{tc} {result}')