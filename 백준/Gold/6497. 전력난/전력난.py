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
    elif x > y:
        parent[x] = y
    else:
        parent[y] = x
    return True


while True:
    m, n = map(int,input().split())
    if not m and not n:
        break
    parent = list(range(m))

    arr = []
    
    sum_cost = 0
    for _ in range(n):
        x, y, z = map(int, input().split())

        arr.append((z, x, y))
        sum_cost += z

    arr.sort()
    
    result = 0
    for dist, a, b in arr:
        if union(a, b):
            result += dist
    
    print(sum_cost - result)