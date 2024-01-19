import sys
input = sys.stdin.readline


def dfs(cnt):
    global ans
    
    pin = 0
    for x in range(5):
        for y in range(9):
            if arr[x][y] == 'o':
                pin += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 9 and arr[nx][ny] == 'o':
                        mx, my = nx + dx, ny + dy
                        if 0 <= mx < 5 and 0 <= my < 9 and arr[mx][my] == '.':
                            arr[x][y] = '.'
                            arr[nx][ny] = '.'
                            arr[mx][my] = 'o'
                            
                            dfs(cnt + 1)
                            
                            arr[x][y] = 'o'
                            arr[nx][ny] = 'o'
                            arr[mx][my] = '.'
    
    ans.add((pin, cnt))
   
    
N = int(input())

for tc in range(N):
    arr = [list(input().strip('\n')) for _ in range(5)]
        
    # dfs 활용
    ans = set()
    
    dfs(0)
    
    print(*sorted(list(ans))[0])
    
    if tc != N - 1:
        cut = input()