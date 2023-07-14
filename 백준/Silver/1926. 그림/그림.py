import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
lst = []

def dfs(x, y):
    global cnt
    cnt += 1
    matrix[x][y] = 0
    for dx, dy in d:
        if -1 < x + dx < n and -1 < y + dy < m and matrix[x + dx][y + dy]:
            dfs(x + dx, y + dy)
    
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