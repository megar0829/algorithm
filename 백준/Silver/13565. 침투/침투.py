import sys
input = sys.stdin.readline
from collections import deque

def bfs(row, col):
    visited = [[0] * M for _ in range(N)]
    que = deque()
    que.append((row, col))
    visited[row][col] = 1
    while que:
        i, j = que.popleft()
        if i == N - 1:
            return True
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and not arr[ni][nj]:
                que.append((ni, nj))
                visited[ni][nj] = 1
    return False


N, M = map(int, input().split())
arr = [list(map(int, input().strip('\n'))) for _ in range(N)]
result = 'NO'

for i in range(M):
    if not arr[0][i]:
        if bfs(0, i):
            result = 'YES'
            break

print(result)