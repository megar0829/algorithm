def dfs(x, y, idx):
    global cnt

    if idx == l + 1:
        cnt += 1
        return

    for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        nx, ny = (x + dx) % N, (y + dy) % M

        if graph[nx][ny] == s[idx]:
            dfs(nx, ny, idx + 1)


N, M, K = map(int, input().split())

graph = [list(input()) for _ in range(N)]

god = []
for _ in range(K):
    S = input()
    if S not in god:
        god.append(S)

for s in god:
    l = len(s) - 1

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == s[0]:
                cnt = 0
                dfs(i, j, 1)
                result += cnt

    print(result)
