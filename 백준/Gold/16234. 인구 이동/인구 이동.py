import sys
input = sys.stdin.readline
from math import trunc
from collections import deque
from pprint import pprint


def bfs(x, y):
    bfs_visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    bfs_visited[x][y] = 1
    save_idx = []
    save_idx.append((x, y))
    save_val = arr[x][y]
    save_cnt = 1
    while queue:
        a, b = queue.popleft()
        for dni, dnj in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            mi, mj = a + dni, b + dnj
            if 0 <= mi < N and 0 <= mj < N:
                if not bfs_visited[mi][mj]:
                    if L <= abs(arr[mi][mj] - arr[a][b]) <= R:
                        queue.append((mi, mj))
                        visited[mi][mj] = 1
                        bfs_visited[mi][mj] = 1
                        save_idx.append((mi, mj))
                        save_val += arr[mi][mj]
                        save_cnt += 1
    avr_val = trunc(save_val / save_cnt)
    sum_lst.append([save_idx, avr_val])


N, L, R = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    flag = False
    visited = [[0] * N for _ in range(N)]
    sum_lst = []

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                for di, dj in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                        if L <= abs(arr[ni][nj] - arr[i][j]) <= R:
                            bfs(i, j)
                            flag = True
    for lst, val in sum_lst:
        for row, col in lst:
            arr[row][col] = val
    if flag:
        result += 1
    else:
        break

print(result)