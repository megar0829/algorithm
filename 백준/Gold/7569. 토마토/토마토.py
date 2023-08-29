import sys
input = sys.stdin.readline
from collections import deque


def bfs(idx):
    global max_val
    que = deque()
    for id in range(len(idx)):
        que.append(idx[id])
        visited[idx[id][0]][idx[id][1]][idx[id][2]] = 1

    while que:
        h, i, j = que.popleft()
        for dh, di, dj in [[0, -1, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]:
            nh, ni, nj = h + dh, i + di, j + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M:
                if not arr[nh][ni][nj] and not visited[nh][ni][nj]:
                    que.append([nh, ni, nj])
                    visited[nh][ni][nj] = visited[h][i][j] + 1

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if not visited[h][n][m]:
                    return False
                if max_val < visited[h][n][m]:
                    max_val = visited[h][n][m]
    return True


M, N, H = list(map(int, input().split()))
arr = []
idx = []
visited = []
max_val = 0
check = True
for h in range(H):
    data = [list(map(int, input().split())) for _ in range(N)]
    arr.append(data)
    visit = [[0] * M for _ in range(N)]
    visited.append(visit)
    for i in range(N):
        for j in range(M):
            if check and data[i][j] == 0:
                check = False

            if data[i][j] == 1:
                idx.append([h, i, j])
            elif data[i][j] == -1:
                visit[i][j] = -1

if check:
    print(0)
else:
    if not bfs(idx):
        print(-1)
    else:
        print(max_val - 1)
