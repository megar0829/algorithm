from collections import deque


def bfs(x, y):
    que = deque()
    visited = [[0] * N for _ in range(N)]
    que.append([x, y])
    visited[x][y] = 1
    while que:
        t = que.popleft()
        i, j = t[0], t[1]
        save_val = arr[i][j]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] < save_val:
                    if visited[ni][nj] == 0:
                        que.append((ni, nj))
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        if visited[ni][nj] < visited[i][j] + 1:
                            que.append((ni, nj))
                            visited[ni][nj] = visited[i][j] + 1
    return visited


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 봉우리 찾기
    max_val = 0
    for i in range(N):
        for j in range(N):
            if max_val < arr[i][j]:
                max_val = arr[i][j]

    # 봉우리의 index 찾아서 리스트에 담아두기
    max_idx = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_val:
                max_idx.append([i, j])

    # visited 최대값 찾기
    # 각각의 봉우리에서 bfs 탐색하여 반환받은
    # visited 배열의 최대값을 구해서 리스트에 담아두기
    max_visit = []
    for i, j in max_idx:
        lst = bfs(i, j)
        save_visit = 0
        for k in range(N):
            if save_visit < max(lst[k]):
                save_visit = max(lst[k])
        max_visit.append(save_visit)

    # 행렬의 모든 값들을 K 만큼 감소시켜서
    # 그때의 각 봉우리에서 visited 최대값 구해서 리스트에 담아두기
    for m in range(1, K + 1):
        for a in range(N):
            for b in range(N):
                save_arr = 0
                if arr[a][b] - m < 0:
                    save_arr = arr[a][b]
                    arr[a][b] = 0
                else:
                    arr[a][b] -= m
                for i, j in max_idx:
                    if arr[i][j] == max_val:
                        lst = bfs(i, j)
                        save_visit = 0
                        for k in range(N):
                            if save_visit < max(lst[k]):
                                save_visit = max(lst[k])
                        max_visit.append(save_visit)
                if not save_arr:
                    arr[a][b] += m
                else:
                    arr[a][b] = save_arr
    print(f'#{tc} {max(max_visit)}')