import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def find_set(x):
    if parent[x] == x:
        return x
    
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    global ans
    
    x, y = find_set(x), find_set(y)
    
    if x == y:
        ans += 1
    
    if x > y:
        parent[x] = y
    
    else:
        parent[y] = x


N, M = map(int, input().split())

parent = list(range(N + 1))

ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    
    union(u, v)

for num in range(1, N):
    if find_set(num) != find_set(num + 1):
        union(num, num + 1)
        ans += 1

print(ans)