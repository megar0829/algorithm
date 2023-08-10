def dfs(n):
    stack = []
    visited[n] = True
    while True:
        for w in range(len(arr[n])):
            if len(arr[n]) and visited[arr[n][w]] == False:
                stack.append(n)
                n = arr[n][w]
                visited[n] = True
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return visited[99]


for _ in range(1, 11):
    tc, E = map(int, input().split())
    edge = list(map(int, input().split()))
    arr = [[] for _ in range(100)]
    visited = [False] * 100
    for i in range(E):
        v1, v2 = edge[i * 2], edge[i * 2 + 1]
        arr[v1].append(v2)
    print(f'#{tc} {int(dfs(0))}')