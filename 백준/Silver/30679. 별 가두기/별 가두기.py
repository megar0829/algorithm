import sys
input = sys.stdin.readline


def check(i, j, d):
    global flag
    
    visited = [[(0, 0) for t in range(M)] for _ in range(N)]
    visited[i][j] = (1, d)
    
    while True:
        val = arr[i][j]
        di, dj = direction[d]
        ni, nj = i + (di * val), j + (dj * val)
        
        if 0 <= ni < N and 0 <= nj < M:
            d = (d + 1) % 4
            if visited[ni][nj] == (1, d):
                break
            
            visited[ni][nj] = (1, d)
            i, j = ni, nj
            
        else:
            flag = False
            break


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

direction = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
}

stars = []

for r in range(N):
    flag = True
        
    check(r, 0, 0)
    
    if flag:
        stars.append(r + 1)

print(len(stars))
print(*sorted(stars))