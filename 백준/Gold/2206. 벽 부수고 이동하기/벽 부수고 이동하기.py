from collections import deque


def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append([0, 0, 0])
    visited[0][0][0] = 1
    while que:
        i, j, check = que.popleft()
        if (i, j) == (N - 1, M - 1):
            return visited[i][j][check]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if not arr[ni][nj] and not visited[ni][nj][check]:
                    que.append([ni, nj, check])
                    visited[ni][nj][check] = visited[i][j][check] + 1
                elif not check:
                    if arr[ni][nj] and not visited[ni][nj][1]:
                        que.append([ni, nj, 1])
                        visited[ni][nj][1] = visited[i][j][check] + 1
    return -1
    

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
min_dis = N * M
print(bfs())