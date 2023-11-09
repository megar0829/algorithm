from collections import deque


def delta(x, y):
    que = deque([(x, y, 1)])
    cnt = 0

    while que:
        x, y, idx = que.popleft()

        if idx == l + 1:
            cnt += 1
            continue

        for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0:
                nx = N - 1
            elif nx >= N:
                nx = 0

            if ny < 0:
                ny = M - 1
            elif ny >= M:
                ny = 0

            if graph[nx][ny] == s[idx]:
                que.append((nx, ny, idx + 1))
    return cnt


N, M, K = map(int, input().split())

graph = [list(input()) for _ in range(N)]

god = []
for _ in range(K):
    S = input()
    if S not in god:
        god.append(S)

for s in god:
    l = len(s) - 1

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == s[0]:
                result += delta(i, j)

    print(result)
