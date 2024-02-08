from collections import deque
import sys
input = sys.stdin.readline


def check(i, j):
    que = deque([(i, j)])
    visited[i][j] = 1
    
    cnt_s, cnt_w = 0, 0
    
    while que:
        x, y = que.popleft()
        
        if arr[x][y] == "o":
            cnt_s += 1
        
        elif arr[x][y] == "v":
            cnt_w += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and arr[nx][ny] != "#":
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                    
    if cnt_s > cnt_w:
        cnt_w = 0
    
    else:
        cnt_s = 0

    cnt_sheep.append(cnt_s)
    cnt_wolf.append(cnt_w)


R, C = map(int, input().split())

arr = [list(input().strip('\n')) for _ in range(R)]

cnt_sheep = [0]
cnt_wolf = [0]

visited = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            if arr[i][j] == "#":
                visited[i][j] = -1
            
            else:
                check(i, j)

print(sum(cnt_sheep), sum(cnt_wolf))