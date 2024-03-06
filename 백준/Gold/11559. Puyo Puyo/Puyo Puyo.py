from collections import deque

def bomb(i, j):
    que = deque([(i, j)])
    visited[i][j] = True
    
    bomb_lst = [(i, j)]
    
    while que:
        x, y = que.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < 12 and 0 <= ny < 6:
                if arr[nx][ny] == arr[i][j] and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    bomb_lst.append((nx, ny))
    
    if len(bomb_lst) >= 4:
        for x, y in bomb_lst:
            arr[x][y] = '.'
        
        return True
    return False


def down():
    
    for c in range(6):
        save_alp = ''
        
        for r in range(11, -1, -1):
            save_alp += arr[r][c]
        
        save_alp = save_alp.replace('.', '')
        
        save_alp += '.' * (12 - len(save_alp))
        
        save_alp = save_alp[::-1]
                
        for r in range(12):
            arr[r][c] = save_alp[r]
            

arr = [list(input()) for _ in range(12)]

ans = 0

while True:
    flag = True

    visited = [[False] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                if bomb(i, j):
                    flag = False
    
    if flag:
        break
    
    ans += 1
    
    down()
    
print(ans)