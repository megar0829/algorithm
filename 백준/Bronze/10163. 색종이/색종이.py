import sys
input = sys.stdin.readline


N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
arr_c = [[] for _ in range(N + 1)]
for a in range(1, N + 1):
    arr_c[a] = list(map(int, input().split()))
    for i in range(arr_c[a][1], arr_c[a][1] + arr_c[a][3]):
        for j in range(arr_c[a][0], arr_c[a][0] + arr_c[a][2]):
            arr[i][j] = a
for a in range(1, N + 1):
    result = 0
    for i in range(arr_c[a][1], arr_c[a][1] + arr_c[a][3]):
        for j in range(arr_c[a][0], arr_c[a][0] + arr_c[a][2]):
            if arr[i][j] == a:
                result += 1
    print(result)


