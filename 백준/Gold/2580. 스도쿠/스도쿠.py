def row_check(row, val):
    for c in range(9):
        if arr[row][c] == val:
            return False
    return True


def col_check(col, val):
    for r in range(9):
        if arr[r][col] == val:
            return False
    return True


def square_check(row, col, val):
    r_idx = (row // 3) * 3
    c_idx = (col // 3) * 3
    for r in range(3):
        for c in range(3):
            if arr[r_idx + r][c_idx + c] == val:
                return False
    return True


def backTracking(cnt):
    if cnt == N:
        for i in range(9):
            print(*arr[i])
        exit()

    for i in range(1, 10):
        x, y = zero_idx[cnt][0], zero_idx[cnt][1]
        if row_check(x, i) and col_check(y, i) and square_check(x, y, i):
            arr[x][y] = i
            backTracking(cnt + 1)
            arr[x][y] = 0


arr = [list(map(int, input().split())) for _ in range(9)]
zero_idx = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            zero_idx.append((i, j))
N = len(zero_idx)
backTracking(0)
