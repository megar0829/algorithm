import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    que = deque([(Hx, Hy, 0, 0)])
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[Hx][Hy][0] = True
    
    while que:
        x, y, move, isMagic = que.popleft()
        
        if (x, y) == (Ex, Ey):
            return move
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny][isMagic]:
                    if arr[nx][ny] and not isMagic:
                        que.append((nx, ny, move + 1, 1))
                        visited[nx][ny][1] = True
                    
                    elif not arr[nx][ny]:
                        que.append((nx, ny, move + 1, isMagic))
                        visited[nx][ny][isMagic] = True

    return -1


N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())

Hx, Hy, Ex, Ey = Hx - 1, Hy - 1, Ex - 1, Ey - 1

arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs())