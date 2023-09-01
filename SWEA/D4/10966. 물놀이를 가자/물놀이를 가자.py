from collections import deque

def bfs(que, visited):
    while que:
        i, j = que.popleft()
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                que.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return visited


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    que = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                que.append((i, j))
                visited[i][j] = 0

    result = bfs(que, visited)
    ans = 0
    for i in range(N):
        ans += sum(result[i])
    print(f'#{tc} {ans}')