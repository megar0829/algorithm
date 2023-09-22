def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x, y = find_set(x), find_set(y)
    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = list(range(N + 1))
    for _ in range(M):
        p1, p2 = map(int, input().split())
        union(p1, p2)

    for i in range(1, N + 1):
        find_set(i)

    result = set(parent)

    print(f'#{tc} {len(result) - 1}')