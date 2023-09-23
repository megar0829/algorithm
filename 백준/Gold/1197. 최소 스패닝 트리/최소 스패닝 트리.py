import sys
input = sys.stdin.readline

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x = parent[x]
    y = parent[y]
    
    if x == y:
        return
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


V, E = map(int, input().split())
parent = list(range(V + 1))

edge = []
for _ in range(E):
    start, end, cost = map(int, input().split())
    edge.append((start, end, cost))
edge.sort(key=lambda x:x[2])

result = 0
for i in range(E):
    s, e, c = edge[i]
    
    if find_set(s) != find_set(e):
        union(s, e)
        result += c

print(result)