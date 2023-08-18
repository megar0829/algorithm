def find_num(n):
    for i in range(1, 14):
        for j in range(1, 14):
            if arr[i][j] == n:
                return i, j


def bfs(start, goal):
    queue = []
    queue.append(start)
    visited[start[0]][start[1]] = 1
    while queue:
        i, j = queue.pop(0)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if visited[ni][nj] == 0 and arr[ni][nj] != 1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    if visited[goal[0]][goal[1]] == 0:
        return 0
    return 1


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
for _ in range(10):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {bfs(find_num(2), find_num(3))}')