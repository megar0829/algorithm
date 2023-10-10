from collections import deque


def search():
    global size, size_cnt, cnt, target, dist

    i, j = target
    arr[i][j] = 0
    cnt += dist
    size_cnt += 1

    save_val = size
    size += size_cnt // size
    size_cnt %= save_val

    target, dist = check_dist(i, j)

    # for i in range(N):
    #     print(*arr[i])
    # print('size:', size)
    # print('cnt:', cnt)
    # print('dist:', dist)
    # print('target:', target)
    # print('--------------------')

    if target != (-1, -1):
        return search()
    return


def check_dist(n, m):
    visited = [[-1] * N for _ in range(N)]
    que = deque()
    que.append((n, m))
    visited[n][m] = 0
    while que:
        i, j = que.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] < 0 and arr[ni][nj] <= size:
                    que.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

    rlt = (-1, -1)
    min_dist = 1e9
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < size and 0 < visited[i][j] < min_dist:
                min_dist = visited[i][j]
                rlt = (i, j)
    return rlt, min_dist


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

si, sj = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si, sj = i, j
            arr[i][j] = 0

cnt = 0
size = 2
size_cnt = 0

target, dist = check_dist(si, sj)

if target != (-1, -1):
    search()

print(cnt)