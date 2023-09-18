from copy import deepcopy


def delta(x, y):
    cross = 0
    d = 1
    idx = set()
    idx.add((x, y))
    size.append((1, {(x, y),}))
    while True:
        cnt = 0
        for dx, dy in [(-d, 0), (d, 0), (0, -d), (0, d)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '#':
                    cnt += 1
        if cnt == 4:
            cross += 1
            for dx, dy in [(-d, 0), (d, 0), (0, -d), (0, d)]:
                nx, ny = x + dx, y + dy
                idx.add((nx, ny))
            d += 1
            idx_lst = deepcopy(idx)
            size.append((1 + cross * 4, idx_lst))
        else:
            break



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
size = []
for i in range(N):
    for j in range(M):
        if 0 < i < N - 1 and 0 < j < M - 1:
            if arr[i][j] == '#':
                delta(i, j)
        else:
            if arr[i][j] == '#':
                size.append((1, {(i, j),}))

size.sort(key=lambda x:x[0], reverse=True)
n = len(size)
result = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if size[i][1].isdisjoint(size[j][1]):
            result.append(size[i][0] * size[j][0])
print(max(result))