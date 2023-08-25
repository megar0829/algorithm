N = int(input())
arr = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def delta(i, j):
    candy = 0
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == arr[i][j]:
                cnt = 2
                mi, mj = i, j
                while True:
                    ni += di[k]
                    nj += dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == arr[i][j]:
                            cnt += 1
                        else:
                            break
                    else:
                        break

                while True:
                    mi -= di[k]
                    mj -= dj[k]
                    if 0 <= mi < N and 0 <= mj < N:
                        if arr[mi][mj] == arr[i][j]:
                            cnt += 1
                        else:
                            break
                    else:
                        break

                if candy < cnt:
                    candy = cnt
    return candy


result = 0
for i in range(N):
    for j in range(N - 1):
        if j == N - 2:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            rlt = max(delta(i, j), delta(i, j +1))
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        else:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            rlt = max(delta(i, j), delta(i, j +1))
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if result < rlt:
            result = rlt

for i in range(N):
    for j in range(N - 1):
        if j == N - 2:
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
            rlt = max(delta(j, i), delta(j + 1, i))
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
        else:
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
            rlt = max(delta(j, i), delta(j +1, i))
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
        if result < rlt:
            result = rlt
print(result)