import sys
sys.setrecursionlimit(10 ** 6)


def right(input_arr):
    global cnt, arr_cnt, row, col
    if 0 <= col < N and input_arr[row][col] == 0:
        input_arr[row][col] = 1
        col += 1
        arr_cnt += 1
        return right(input_arr)
    cnt += 1
    if arr_cnt >= M * N:
        return cnt
    col -= 1
    row += 1
    return down(input_arr)


def down(input_arr):
    global cnt, arr_cnt, row, col
    if 0 <= row < M and input_arr[row][col] == 0:
        input_arr[row][col] = 1
        row += 1
        arr_cnt += 1
        return down(input_arr)
    cnt += 1
    if arr_cnt >= M * N:
        return cnt
    row -= 1
    col -= 1
    return left(input_arr)


def left(input_arr):
    global cnt, arr_cnt, row, col
    if 0 <= col < N and input_arr[row][col] == 0:
        input_arr[row][col] = 1
        col -= 1
        arr_cnt += 1
        return left(input_arr)
    cnt += 1
    if arr_cnt >= M * N:
        return cnt
    col += 1
    row -= 1
    return up(input_arr)


def up(input_arr):
    global cnt, arr_cnt, row, col
    if 0 <= row < M and input_arr[row][col] == 0:
        input_arr[row][col] = 1
        row -= 1
        arr_cnt += 1
        return up(input_arr)
    cnt += 1
    if arr_cnt >= M * N:
        return cnt
    row += 1
    col += 1
    return right(input_arr)


M, N = map(int, input().split())
arr = [[0] * N for _ in range(M)]
arr_cnt = 0
cnt = 0
row, col = 0, 0
print(right(arr) - 1)