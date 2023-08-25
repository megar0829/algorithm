import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
arr_c = [[] for _ in range(N + 1)]
result = [0] * N
for a in range(1, N + 1):
    arr_c[a] = list(map(int, input().split()))
    for i in range(arr_c[a][1], arr_c[a][1] + arr_c[a][3]):
        for j in range(arr_c[a][0], arr_c[a][0] + arr_c[a][2]):
            if arr[i][j] == 0:
                arr[i][j] = a
                result[a - 1] += 1
            else:
                result[arr[i][j] - 1] -= 1
                arr[i][j] = a
                result[a - 1] += 1

for a in range(1, N + 1):
    print(result[a - 1])