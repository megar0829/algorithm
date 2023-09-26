def dfs(i, j, dist):
    global cnt
    if i == 0 and j == C - 1:
        if dist == K:
            cnt += 1
        return
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C:
            if arr[ni][nj] != 'T' and not visited[ni][nj]:
                visited[i][j] = 1
                dfs(ni, nj, dist + 1)
                visited[i][j] = 0


R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
cnt = 0
visited[R - 1][0] = 1
dfs(R - 1, 0, 1)

print(cnt)