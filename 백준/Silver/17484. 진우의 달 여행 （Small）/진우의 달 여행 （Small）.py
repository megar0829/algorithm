N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

direction = [-1, 0, 1]

def dfs(i, j, d, min_value, save_value):
    if i == N - 1:
        return min(min_value, save_value)
    for k in direction:
        if k != d:
            if 0 <= i < N and 0 <= j + k < M:
                min_value = dfs(i + 1, j + k, k, min_value, save_value + arr[i + 1][j + k])
    return min_value

min_val = 1e9
for i in range(M):
    min_val = min(dfs(0, i, 2, min_val, arr[0][i]), min_val)

print(min_val)