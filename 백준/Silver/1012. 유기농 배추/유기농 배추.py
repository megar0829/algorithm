import sys
input = sys.stdin.readline

def delta(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = []
    stack.append([x, y])
    arr[y][x] = 0
    while stack:
        x, y = stack.pop()
        arr[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[ny][nx] == 1:
                    stack.append([nx, ny])
        else:
            continue
    return


T = int(input())
for _ in range(T):
    M, N, K = list(map(int, input().split()))
    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                result += 1
                delta(j, i)
    print(result)