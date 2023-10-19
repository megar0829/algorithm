import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def find_set(x):
    if parent[x] == x:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    if x < y:
        parent[y] = x
    elif x > y:
        parent[x] = y


n, m = map(int, input().split())
parent = list(range(n))
flag = True
for num in range(m):
    p1, p2 = map(int, input().split())

    x, y = find_set(p1), find_set(p2)
    if x == y:
        flag = False
        print(num + 1)
        break
    else:
        union(x, y)

if flag:
    print(0)