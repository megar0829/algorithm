import sys
input = sys.stdin.readline


def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x, y = find_set(x), find_set(y)

    if x == y:
        return True
    elif x > y:
        parent[x] = y
    elif x < y:
        parent[y] = x
    return False


n = int(input())
node = {}
for num in range(1, n + 1):
    x, y = map(float, input().split())
    node[num] = (x, y)

parent = list(range(n + 1))

arr = []

for i in range(1, n):
    for j in range(i, n + 1):
        x, y = node[i]
        nx, ny = node[j]
        dist = ((x - nx) ** 2 + (y - ny) ** 2) ** 0.5

        arr.append((dist, i, j))

arr.sort()

result = 0
for dist, now, next in arr:
    if not union(now, next):
        result += dist
        
print(round(result, 2))
