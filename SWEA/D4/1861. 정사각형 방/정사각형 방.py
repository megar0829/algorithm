def bfs(s1, s2):
    que = []
    visited = [[0] * N for _ in range(N)]
    que.append((s1, s2))
    visited[s1][s2] = 1
    max_visit = 1
    while que:
        i, j = que.pop(0)
        max_visit = max(visited[i][j], max_visit)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and arr[ni][nj] == arr[i][j] + 1:
                    que.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return max_visit


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    max_idx = 1000000
    for i in range(N):
        for j in range(N):
            save_val = bfs(i, j)
            if max_val < save_val:
                max_val = save_val
                max_idx = arr[i][j]
            elif max_val == save_val:
                max_idx = min(max_idx, arr[i][j])

    print(f'#{tc} {max_idx} {max_val}')