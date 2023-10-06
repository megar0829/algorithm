# 1743 s1
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global max_size
    que = deque()
    visited[x][y] = 1
    que.append((x, y))
    size = 1
    while que:
        i, j = que.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and arr[ni][nj]:
                    que.append((ni, nj))
                    visited[ni][nj] = 1
                    size += 1
    max_size = max(max_size, size)


N, M ,K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

visited = [[0] * M for _ in range(N)]
max_size = 0

for row in range(N):
    for col in range(M):
        if arr[row][col]:
            bfs(row, col)

print(max_size)