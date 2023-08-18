import sys
input = sys.stdin.readline


def bfs(x, y):
    que = []
    que.append((x, y))
    visited[x][y] = 1
    cnt = 0
    while que:
        i, j = que.pop(0)
        cnt += 1
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    que.append((ni, nj))
                    visited[ni][nj] = 1
    return cnt


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N = int(input())
arr = [list(map(int, input().strip('\n'))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = []
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            result.append(bfs(i, j))
print(cnt)
for i in sorted(result):
    print(i)