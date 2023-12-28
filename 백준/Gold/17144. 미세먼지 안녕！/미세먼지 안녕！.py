from copy import deepcopy
import sys
input = sys.stdin.readline


def start_air_cleaner(): 
    # 공기청정기 위쪽 
    copy_room = deepcopy(room)
    
    i, j = air_cleaner_top, 1
    
    room[i][j] = 0
    
    for di, dj in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        ni, nj = i + di, j + dj
        
        while True:            
            if (ni, nj) == (air_cleaner_top, 0):
                break
            
            if 0 <= ni < R and 0 <= nj < C:
                room[ni][nj] = copy_room[ni - di][nj - dj]
                
            else:
                break
            
            ni += di
            nj += dj
            
        i, j = ni - di, nj - dj 

    # 공기청정기 아래쪽

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = air_cleaner_bot, 1
    
    room[x][y] = 0
    
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        
        while True:
            if (nx, ny) == (air_cleaner_bot, 0):
                break
            
            if 0 <= nx < R and 0 <= ny < C:
                room[nx][ny] = copy_room[nx - dx][ny - dy]
             
            else:
                break
           
            nx += dx
            ny += dy
        
        x, y = nx - dx, ny - dy


def spread_of_dust():       
    for r in range(R):
        for c in range(C): 
            if room[r][c] > 0:
                cnt_spread = 0
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < R and 0 <= nc < C:
                        if room[nr][nc] != -1:
                            copy_room[nr][nc] += room[r][c] // 5
                            cnt_spread += 1
                
                copy_room[r][c] -= (room[r][c] // 5) * cnt_spread
    

R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]


for i in range(R):
    if room[i][0] == -1:
        air_cleaner_top = i
        air_cleaner_bot = i + 1
        break


for _ in range(T):
    copy_room = deepcopy(room)
    
    spread_of_dust()
    
    room = deepcopy(copy_room)
    
    start_air_cleaner()

cnt = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            cnt += room[i][j]

print(cnt)