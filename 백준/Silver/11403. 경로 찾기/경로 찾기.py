def dfs(s, e):
    visited = [0] * N
    stack = []
    stack.append(s)
    visited[s] = 1
    if s == e:
        visited[s] = 0
    t = s
    while stack:
        for w in range(N):
            if arr[t][w] == 1 and not visited[w]:
                stack.append(w)
                visited[w] = 1
                continue
        else:
            if stack:
                t = stack.pop()

    if visited[e] == 1:
        return True
    return False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if dfs(i, j):
            result[i][j] = 1

for i in range(N):
    print(*result[i])