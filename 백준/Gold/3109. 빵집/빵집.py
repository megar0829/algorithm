import sys
input = sys.stdin.readline


def dfs(i, j):
    global result, flag

    if j == C - 1:
        visited[i][j] = 1
        result += 1
        flag = True
        return

    visited[i][j] = 1

    for di, dj in [(-1, 1), (0, 1), (1, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C:
            if not visited[ni][nj] and arr[ni][nj] != 'x':
                dfs(ni, nj)
                if flag:
                    return
    if flag:
        return


R, C = map(int, input().split())

arr = [list(input().strip('\n')) for _ in range(R)]

visited = [[0] * C for _ in range(R)]

result = 0

for r in range(R):
    flag = False
    dfs(r, 0)

print(result)