from copy import deepcopy
import sys
input = sys.stdin.readline


def bfs(start, end, color, input_arr):
    visited = [[0] * N for _ in range(N)]
    que = []
    que.append((start, end))
    visited[start][end] = 1
    input_arr[start][end] = 0
    while que:
        i, j = que.pop(0)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if input_arr[ni][nj] == color and visited[ni][nj] == 0:
                    input_arr[ni][nj] = 0
                    que.append((ni, nj))
                    visited[ni][nj] = 1
    return input_arr
                         

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N = int(input())
arr = [list(input()) for _ in range(N)]
arr_green = deepcopy(arr)
colors = ['R', 'G', 'B']
cnt = 0
cnt_green = 0
for i in range(N):
    for j in range(N):
        if arr_green[i][j] == 'G':
            arr_green[i][j] = 'R'


for i in range(N):
    for j in range(N):
        if arr[i][j] in colors:
            arr = bfs(i, j, arr[i][j], arr)
            cnt += 1
        if arr_green[i][j] in colors:
            arr_green = bfs(i, j, arr_green[i][j], arr_green)
            cnt_green += 1

print(cnt, cnt_green)