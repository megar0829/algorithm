import sys
input = sys.stdin.readline


def dfs(x, y):
    stack = []
    stack.append([x, y])
    while stack:
        x, y = stack.pop()
        arr[y][x] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[ny][nx] == 1:
                    stack.append([nx, ny])
        else:
            continue
    return



dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    M, N = map(int, input().split())
    if N == 0 and M == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                result += 1
                dfs(j, i)
    print(result)