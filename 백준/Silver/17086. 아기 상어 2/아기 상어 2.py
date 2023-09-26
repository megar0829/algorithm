import sys
input = sys.stdin.readline
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    while que:
        i, j = que.popleft()
        for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] or visited[ni][nj] > visited[i][j] + 1:
                    if arr[ni][nj]:
                        return visited[i][j]
                    que.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_val = 0
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            max_val = max(max_val, bfs(i, j))

print(max_val)