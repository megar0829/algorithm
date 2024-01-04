import sys
input = sys.stdin.readline
import heapq

def find_set(x):
    if parent[x] == x:
        return x
    
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x, y = find_set(x), find_set(y)
    
    if x >= y:
        parent[x] = y
    else:
        parent[y] = x


p, w = map(int, input().split())

c, v = map(int, input().split())

pq = []

for _ in range(w):
    start, end, width = map(int, input().split())
    
    heapq.heappush(pq, (-width, start, end))
    
result = 0

parent = list(range(p))

while pq:
    length, x, y = heapq.heappop(pq)
    
    union(x, y)

    if find_set(c) == find_set(v):
        result = -length
        break

print(result)