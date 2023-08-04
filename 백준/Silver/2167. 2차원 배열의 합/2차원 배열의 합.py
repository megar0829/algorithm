import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sum_arr = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_arr[i][j] = arr[i - 1][j - 1] + sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1]
K = int(input())
for _ in range(K):
    i, j, x, y = list(map(int, input().split()))
    result = sum_arr[x][y] - sum_arr[x][j - 1] - sum_arr[i - 1][y] + sum_arr[i - 1][j - 1]
    print(result)
