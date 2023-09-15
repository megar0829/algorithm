import sys
input = sys.stdin.readline

while True:
    text = input().strip('\n')
    if text == 'end':
        break
    arr = []
    for i in range(3):
        arr.append([text[i * 3], text[i * 3 + 1], text[i * 3 + 2]])

    flag = False
    X_end_check = False
    O_end_check = False
    true_check = False
    false_check = False

    O_cnt = 0
    X_cnt = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 'O':
                O_cnt += 1
            elif arr[i][j] == 'X':
                X_cnt += 1

    # 행우선, 열우선 탐색
    for i in range(3):
        col_O_cnt = 0
        col_X_cnt = 0
        row_O_cnt = 0
        row_X_cnt = 0
        for j in range(3):
            if arr[i][j] == 'O':
                row_O_cnt += 1
            elif arr[i][j] == 'X':
                row_X_cnt += 1

            if arr[j][i] == 'O':
                col_O_cnt += 1
            elif arr[j][i] == 'X':
                col_X_cnt += 1
        if (row_O_cnt == 3 or col_O_cnt == 3):
            if X_cnt == O_cnt:
                O_end_check = True
            else:
                false_check = True
        elif (row_X_cnt == 3 or col_X_cnt == 3):
            if X_cnt > O_cnt:
                X_end_check = True
            else:
                false_check = True

    s_O_cnt = 0
    s_X_cnt = 0
    r_O_cnt = 0
    r_X_cnt = 0
    for i in range(3):
        if arr[i][i] == 'O':
            s_O_cnt += 1
        elif arr[i][i] == 'X':
            s_X_cnt += 1

        if arr[i][2 - i] == 'O':
            r_O_cnt += 1
        elif arr[i][2 - i] == 'X':
            r_X_cnt += 1
    if (s_O_cnt == 3 or r_O_cnt == 3):
        if X_cnt == O_cnt:
            O_end_check = True
        else:
            false_check = True
    elif (s_X_cnt == 3 or r_X_cnt == 3):
        if X_cnt > O_cnt:
            X_end_check = True
        else:
            false_check = True

    if O_cnt + X_cnt == 9:
        if O_cnt == 4 and X_cnt == 5:
            flag = True
            true_check = True
    else:
        if X_cnt - O_cnt == 1 or O_cnt == X_cnt:
            flag = True
    # for i in range(3):
    #     print(arr[i])
    # print(O_end_check)
    # print(X_end_check)

    if false_check or (O_end_check and X_end_check):
        print('invalid')
    elif (flag and X_end_check) or (not X_end_check and true_check):
        print('valid')
    elif (flag and O_end_check) or (not O_end_check and true_check):
        print('valid')
    else:
        print('invalid')