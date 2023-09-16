import sys
input = sys.stdin.readline
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = 0
    while que:
        i, j = que.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if visited[ni][nj] == -1:
                    if arr[ni][nj]:
                        que.append((ni, nj))
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        visited[ni][nj] = 0
                        
    for i in range(n):
        for j in range(m):
            if visited[i][j] == -1 and not arr[i][j]:
                visited[i][j] = 0
    


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
flag = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)
            flag = True
            break
    if flag:
        break

for visit in visited:
    print(*visit)