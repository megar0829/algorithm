def delta(x, y):
    sum_val = arr[x][y]
    sum_idx = set()
    sum_idx.add((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        sum_val += arr[nx][ny]
        sum_idx.add((nx, ny))
    return sum_val, sum_idx


def delta_check(a, b, c):
    flag = True
    if not a.isdisjoint(b):
        flag = False
    if not b.isdisjoint(c):
        flag = False
    if not c.isdisjoint(a):
        flag = False
    return flag


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]

min_i, min_j = 0, 0
min_lst = []
for i in range(1, N - 1):
    for j in range(1, N - 1):
        save_val, save_idx = delta(i, j)
        min_lst.append([save_val, save_idx])

min_lst.sort(key=lambda x:x[0])
M = len(min_lst)
min_val = 1e9
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            if delta_check(min_lst[i][1], min_lst[j][1], min_lst[k][1]):
                min_val = min(min_val, (min_lst[i][0] + min_lst[j][0] + min_lst[k][0]))
print(min_val)