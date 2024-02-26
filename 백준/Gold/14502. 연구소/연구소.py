import sys
input = sys.stdin.readline

from collections import deque
from copy import deepcopy

def bfs():
    global result
    que = deque()
    
    copy_arr = deepcopy(arr)
    
    for r in range(N):
        for c in range(M):
            if copy_arr[r][c] == 2:
                que.append((r, c))


    while que:
        x, y = que.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not copy_arr[nx][ny]:
                que.append((nx, ny))
                copy_arr[nx][ny] = 2

    c = 0
    for x in range(N):
        for y in range(M):
            if not copy_arr[x][y]:
                c += 1

    result = max(result, c)


def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                arr[i][j] = 1
                dfs(cnt + 1)
                arr[i][j] = 0
                

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

dfs(0)

print(result)
