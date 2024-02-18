import sys
input = sys.stdin.readline
from copy import deepcopy

def func1():
    lst = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            lst[(N - 1) - i][j] = arr[i][j]

    return deepcopy(lst)


def func2():
    lst = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            lst[i][(M - 1) - j] = arr[i][j]

    return deepcopy(lst)


def func3():
    lst = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            lst[j][(N - 1) - i] = arr[i][j]

    return deepcopy(lst)


def func4():
    lst = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            lst[(M - 1) - j][i] = arr[i][j]

    return deepcopy(lst)


def func5():
    lst = [[0] * M for _ in range(N)]

    save_val = []
    idx = -1
    for n in range(2):
        for m in range(2):
            idx += 1
            save_val.append([])
            for i in range(n * (N // 2), (n + 1) * (N // 2)):
                for j in range(m * (M // 2), (m + 1) * (M // 2)):
                    save_val[idx].append(arr[i][j])

    save_val = [save_val[2], save_val[0], save_val[3], save_val[1]]

    idx = -1
    for n in range(2):
        for m in range(2):
            idx += 1
            v = 0
            for i in range(n * (N // 2), (n + 1) * (N // 2)):
                for j in range(m * (M // 2), (m + 1) * (M // 2)):
                    lst[i][j] = save_val[idx][v]
                    v += 1
    return deepcopy(lst)


def func6():
    lst = [[0] * M for _ in range(N)]

    save_val = []
    idx = -1
    for n in range(2):
        for m in range(2):
            idx += 1
            save_val.append([])
            for i in range(n * (N // 2), (n + 1) * (N // 2)):
                for j in range(m * (M // 2), (m + 1) * (M // 2)):
                    save_val[idx].append(arr[i][j])

    save_val = [save_val[1], save_val[3], save_val[0], save_val[2]]

    idx = -1
    for n in range(2):
        for m in range(2):
            idx += 1
            v = 0
            for i in range(n * (N // 2), (n + 1) * (N // 2)):
                for j in range(m * (M // 2), (m + 1) * (M // 2)):
                    lst[i][j] = save_val[idx][v]
                    v += 1
    return deepcopy(lst)




N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

func_lst = list(map(int, input().split()))

for func_num in func_lst:
    if func_num == 1:
        arr = func1()

    elif func_num == 2:
        arr = func2()

    elif func_num == 3:
        arr = func3()
        N, M = M, N

    elif func_num == 4:
        arr = func4()
        N, M = M, N

    elif func_num == 5:
        arr = func5()

    elif func_num == 6:
        arr = func6()

for i in range(N):
    print(*arr[i])