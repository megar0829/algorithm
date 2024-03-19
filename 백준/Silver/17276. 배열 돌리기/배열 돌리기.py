from copy import deepcopy
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    lines = []
    
    mi, mj = (n // 2, n // 2)
    
    for i in range(n // 2, 0, -1):
        line = []
        
        for di, dj in [(-i, 0), (-i, i), (0, i), (i, i), (i, 0), (i, -i), (0, -i), (-i, -i)]:
            line.append((mi + di, mj + dj))
        
        if d < 0:        
            lines.append(line[::-1])
        else:
            lines.append(line[:])

    for _ in range(abs(d) // 45):
        save_arr = deepcopy(arr)
        
        for i in range(n // 2):
            for j in range(8):
                now_i, now_j = lines[i][j]
                
                next_i, next_j = lines[i][(j + 1) % 8]
                
                arr[next_i][next_j] = save_arr[now_i][now_j]
                
    for i in range(n):
        print(*arr[i])