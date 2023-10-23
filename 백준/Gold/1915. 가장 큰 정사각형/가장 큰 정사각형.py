import sys
input = sys.stdin.readline

# 현재 값의 왼쪽 위, 왼쪽, 위의 값들이 모두 같다면 하나의 정사각형이라 판단
def check(x, y):
    if 0 < x < n and 0 < y < m:
        return min(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1]) + 1
    return 1


n, m = map(int, input().split())
arr = [list(map(int, input().strip('\n'))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

max_val = 0

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            dp[i][j] = check(i, j)
            max_val = max(max_val, dp[i][j] ** 2)

print(max_val)



# from collections import deque
#
#
# def check(val, x, y):
#     size = (val + 1) // 2
#     for r in range(x, x - size, -1):
#         for c in range(y, y - size, -1):
#             if not arr[r][c]:
#                 return False
#     return True
#
#
# def bfs(row, col):
#     global max_val
#
#     visited = [[0] * m for _ in range(n)]
#     que = deque()
#     que.append((row, col))
#     visited[row][col] = 1
#
#     while que:
#         i, j = que.popleft()
#         if visited[i][j] > 2 and visited[i][j] % 2:
#             if arr[i - 1][j] and arr[i][j - 1] and arr[i - 1][j - 1]:
#                 if check(visited[i][j], i, j):
#                     max_val = max(max_val, ((visited[i][j] + 1 ) // 2) ** 2)
#
#         for di, dj in [(0, 1), (1, 0)]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] and not visited[ni][nj]:
#                 que.append((ni, nj))
#                 visited[ni][nj] = visited[i][j] + 1
#
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().strip('\n'))) for _ in range(n)]
# max_val = 1
#
# for i in range(n - 1):
#     for j in range(m - 1):
#         if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]:
#             bfs(i, j)
#
# sum_val = 0
# for i in range(n):
#     sum_val += sum(arr[i])
#
# if sum_val:
#     print(max_val)
# else:
#     print(0)
#
