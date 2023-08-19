import sys
input = sys.stdin.readline
from collections import deque


def bfs(lst):
    n = len(lst)
    que = deque()
    for i in range(n):
        que.append(lst[i])
        visited[lst[i][0]][lst[i][1]] = 1
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    que.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    cnt = 0
    max_val = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
               if max_val < visited[i][j]:
                   max_val = visited[i][j]
            else:
                return -1
    return max_val - 1
    


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
tomato = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
           tomato.append((i, j)) 
        if arr[i][j] == -1:
            visited[i][j] = 1
print(bfs(tomato))
