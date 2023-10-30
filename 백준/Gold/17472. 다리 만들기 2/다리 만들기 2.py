import sys
input = sys.stdin.readline
from collections import deque


def bfs(x, y, val):
    que = deque([(x, y)])

    while que:
        r, c = que.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] and not parent[nr][nc]:
                    que.append((nr, nc))
                    parent[nr][nc] = val
                    

def check_bridge(x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not arr[nx][ny]:
                cnt = 0
                flag = False
                    
                while 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny]:
                        flag = True
                        break
                    nx += dx
                    ny += dy
                    cnt += 1
                
                if flag and parent[x][y] != parent[nx][ny] and cnt >= 2:
                    edge.append((cnt, parent[x][y], parent[nx][ny]))
           
           
def find_set(x):
    if parent_num[x] == x:
        return x
    
    parent_num[x] = find_set(parent_num[x])
    return parent_num[x]


def union(x, y):
    x, y = find_set(x), find_set(y)
    
    if x == y:
        return False
    elif x < y:
        parent_num[y] = x
    else:
        parent_num[x] = y
    return True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

parent = [[0] * M for _ in range(N)]

num = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] and not parent[i][j]:
            parent[i][j] = num
            bfs(i, j, num)
            num += 1


edge = []
for i in range(N):
    for j in range(M):
         if arr[i][j]:
             check_bridge(i, j)

edge.sort()

parent_num = list(range(num))
result = 0
if not edge:
    print(-1)
else:
    for dist, i1, i2 in edge:
        if union(i1, i2):
            result += dist

    save_val = find_set(1)
    flag = False
    for i in range(2, num):
        if find_set(i) != save_val:
            flag = True
    
    if flag:
        print(-1)
    else:
        print(result)