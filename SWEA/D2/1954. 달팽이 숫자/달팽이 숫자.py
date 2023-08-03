def right(arr):
    global i, j, cnt
    if (0 <= i < N and 0 <= j < N) \
            and arr[i][j] == 0:
        cnt += 1
        arr[i][j] = cnt
        j += 1
        return right(arr)
    j -= 1
    i += 1
    if cnt == N ** 2:
        return arr
    return down(arr)


def left(arr):
    global i, j, cnt
    if (0 <= i < N and 0 <= j < N) \
            and arr[i][j] == 0:
        cnt += 1
        arr[i][j] = cnt
        j -= 1
        return left(arr)
    j += 1
    i -= 1
    if cnt == N ** 2:
        return arr
    return up(arr)


def up(arr):
    global i, j, cnt
    if (0 <= i < N and 0 <= j < N) \
            and arr[i][j] == 0:
        cnt += 1
        arr[i][j] = cnt
        i -= 1
        return up(arr)
    i += 1
    j += 1
    if cnt == N ** 2:
        return arr
    return right(arr)


def down(arr):
    global i, j, cnt
    if (0 <= i < N and 0 <= j < N) \
            and arr[i][j] == 0:
        cnt += 1
        arr[i][j] = cnt
        i += 1
        return down(arr)
    i -= 1
    j -= 1
    if cnt == N ** 2:
        return arr
    return left(arr)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    i, j, cnt = 0, 0, 0
    arr = right(arr)
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
