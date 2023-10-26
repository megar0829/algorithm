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
        return False

    elif x < y:
        parent[y] = x
    else:
        parent[x] = y
    return True


N, M = map(int, input().split())
parent = list(range(N + 1))

gods = []
for num in range(N):
    X, Y = map(int, input().split())
    gods.append((X, Y, num + 1))
gods.sort()

for _ in range(M):
    n1, n2 = map(int, input().split())
    union(n1, n2)

edge = []
for i in range(N - 1):
    for j in range(i + 1, N):
        dist = ((gods[i][0] - gods[j][0]) ** 2 + (gods[i][1] - gods[j][1]) ** 2) ** 0.5
        edge.append((dist, gods[i][2], gods[j][2]))
edge.sort()

result = 0
for dist, g1, g2 in edge:
    if union(g1, g2):
        result += dist

print(format(round(result, 2), ".2f"))