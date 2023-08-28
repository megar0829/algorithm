def bfs(R, C, L):
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    que = []
    que.append([R, C])
    while que:
        i, j = que.pop(0)
        if arr[i][j] == 1:
            for direc in [u, d, l, r]:
                ni, nj = i + direc[0], j + direc[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] and not visited[ni][nj]:
                        if (direc == u and (arr[ni][nj] in up)) \
                                or (direc == d and (arr[ni][nj] in down)) \
                                or (direc == l and (arr[ni][nj] in left)) \
                                or (direc == r and (arr[ni][nj] in right)):
                            que.append([ni, nj])
                            visited[ni][nj] = visited[i][j] + 1

        elif arr[i][j] == 2:
            for direc in [u, d]:
                ni, nj = i + direc[0], j + direc[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] and not visited[ni][nj]:
                        if (direc == u and (arr[ni][nj] in up)) \
                                or (direc == d and (arr[ni][nj] in down)):
                            que.append([ni, nj])
                            visited[ni][nj] = visited[i][j] + 1

        elif arr[i][j] == 3:
            for direc in [l, r]:
                ni, nj = i + direc[0], j + direc[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] and not visited[ni][nj]:
                        if (direc == l and (arr[ni][nj] in left)) \
                                or (direc == r and (arr[ni][nj] in right)):
                            que.append([ni, nj])
                            visited[ni][nj] = visited[i][j] + 1

        elif arr[i][j] == 4:
            for direc in [u, r]:
                ni, nj = i + direc[0], j + direc[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] and not visited[ni][nj]:
                        if (direc == u and (arr[ni][nj] in up)) \
                                or (direc == r and (arr[ni][nj] in right)):
                            que.append([ni, nj])
                            visited[ni][nj] = visited[i][j] + 1

        elif arr[i][j] == 5:
            for direc in [r, d]:
                ni, nj = i + direc[0], j + direc[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] and not visited[ni][nj]:
                        if (direc == r and (arr[ni][nj] in right)) \
                                or (direc == d and (arr[ni][nj] in down)):
                            que.append([ni, nj])
                            visited[ni][nj] = visited[i][j] + 1

        elif arr[i][j] == 6:
            for direc in [l, d]:
                ni, nj = i + direc[0], j + direc[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] and not visited[ni][nj]:
                        if (direc == l and (arr[ni][nj] in left)) \
                                or (direc == d and (arr[ni][nj] in down)):
                            que.append([ni, nj])
                            visited[ni][nj] = visited[i][j] + 1

        elif arr[i][j] == 7:
            for direc in [l, u]:
                ni, nj = i + direc[0], j + direc[1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] and not visited[ni][nj]:
                        if (direc == l and (arr[ni][nj] in left)) \
                                or (direc == u and (arr[ni][nj] in up)):
                            que.append([ni, nj])
                            visited[ni][nj] = visited[i][j] + 1
    cnt = 0
    for x in range(N):
        for y in range(M):
            if 0 < visited[x][y] <= L:
                cnt += 1
    return cnt


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

l = [0, -1]
r = [0, 1]
u = [-1, 0]
d = [1, 0]

left = [1, 3, 4, 5]
right = [1, 3, 6, 7]
up = [1, 2, 5, 6]
down = [1, 2, 4, 7]

T = int(input())


for tc in range(1, T + 1):
    N, M, R, C, L = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bfs(R, C, L)}')