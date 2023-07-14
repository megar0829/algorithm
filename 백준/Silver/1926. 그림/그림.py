import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
lst = []

def dfs(x, y):
    global cnt
    cnt += 1
    matrix[x][y] = 0
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if -1 < nx < n and -1 < ny < m and matrix[nx][ny]:
            dfs(nx, ny)
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            cnt = 0
            dfs(i, j)
            lst.append(cnt)
if len(lst) == 0:
    print(0)
    print(0)
else:
    print(len(lst))
    print(max(lst))