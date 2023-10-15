import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    
    if x == y:
        return
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    

N = int(input())
M = int(input())
parent = list(range(N + 1))
graph = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union(i + 1, j + 1)

save_val = find(arr[0])
flag = True
for city in arr:
    if find(city) != save_val:
        print('NO')
        flag = False
        break
    
if flag:
    print('YES')