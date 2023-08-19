import sys
input = sys.stdin.readline


def bfs(x, y):
    que = []
    que.append((x, y))
    visited[x][y] = 1
    while que:
        i, j = que.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    que.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                    

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().strip('\n'))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
bfs(0, 0)
print(visited[N - 1][M - 1])