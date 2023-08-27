from collections import deque


def bfs(x, y):
    que = deque()
    que.append([x, y])
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    arr[x][y] = 0
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] and not visited[ni][nj]:
                    que.append([ni, nj])
                    arr[ni][nj] = 0
                    visited[ni][nj] = visited[i][j] + 1
    max_val = 0
    for i in range(N):
        for j in range(N):
            if max_val < visited[i][j]:
                max_val = visited[i][j]
                ni, nj = i, j
    
    return ni, nj
        

T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                cnt += 1
                w, h = bfs(i, j)
                w, h = w - i + 1, h - j + 1
                result.append([w * h, w, h])
    
    rlt = [cnt] 
    for s, w, h in sorted(result):
        rlt.append(w)
        rlt.append(h)
        
    print(f'#{tc}', *rlt)