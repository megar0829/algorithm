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
    

n, m = map(int, input().split())
parent = list(range(n + 1))

for _ in range(m):
    num, a, b = map(int, input().split())
    if num:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)