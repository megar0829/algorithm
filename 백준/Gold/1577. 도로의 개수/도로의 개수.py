import sys
input = sys.stdin.readline


# 1. dfs 사용

# def dfs(i, j, cnt):
#     global result

#     if (i, j) == (N, M):
#         result += 1
#         return

#     if cnt >= N + M:
#         return

#     for di, dj in [(0, 1), (1, 0)]:
#         ni, nj = i + di, j + dj

#         if 0 <= ni <= N and 0 <= nj <= M:
#             load.setdefault((ni, nj), 0)
#             if load[(i, j)] != (ni, nj):
#                 dfs(ni, nj, cnt + 1)


# N, M = map(int, input().split())

# arr = [[0] * (M + 1) for _ in range(N + 1)]

# load = dict()

# # 도로에 공사중인 곳 표시
# K = int(input())
# for _ in range(K):
#     a, b, c, d = map(int, input().split())

#     if a == c:
#         load[(a, min(b, d))] = (a, max(b, d))

#     elif b == d:
#         load[(min(a, c), b)] = (max(a, c), b)

# result = 0

# load.setdefault((0, 0), 0)

# dfs(0, 0, 0)

# print(result)


# 2. DP 사용

N, M = map(int, input().split())
DP = [[[0, [True, True]] for _ in range(M + 1)] for _ in range(N + 1)]
DP[0][0][0] = 1

K = int(input())

for _ in range(K):
    a, b, c, d = map(int, input().split())

    if a > c:
        a, c = c, a

    if b > d:
        b, d = d, b

    if c - a > d - b:
        d = 0
    else:
        d = 1

    DP[a][b][1][d] = False

for x in range(N + 1):
    for y in range(M + 1):

        nx, ny = x + 1, y
        if 0 <= nx <= N and 0 <= ny <= M and DP[x][y][1][0]:
            DP[nx][ny][0] += DP[x][y][0]

        nx, ny = x, y + 1
        if 0 <= nx <= N and 0 <= ny <= M and DP[x][y][1][1]:
            DP[nx][ny][0] += DP[x][y][0]

print(DP[N][M][0])