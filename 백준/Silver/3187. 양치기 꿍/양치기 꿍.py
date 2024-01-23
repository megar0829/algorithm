import sys
input = sys.stdin.readline
from collections import deque

def check(r, c):
    global w, s
    
    que = deque([(r, c)])
    visited[r][c] = 1
    
    save_w, save_s = 0, 0
    
    while que:
        x, y = que.popleft()
        
        if arr[x][y] == 'v':
            save_w += 1
        elif arr[x][y] == 'k':
            save_s += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and arr[nx][ny] != '#':
                    que.append((nx, ny))
                    visited[nx][ny] = 1
    
    if save_w >= save_s:
        s -= save_s
    
    else:
        w -= save_w


R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

visited = [[0] * C for _ in range(R)]

w, s = 0, 0

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'v':
            w += 1
        elif arr[i][j] == 'k':
            s += 1


for i in range(R):
    for j in range(C):
        if not visited[i][j] and arr[i][j] != '#':
            check(i, j)
            
print(s, w)