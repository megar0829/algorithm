import sys
input = sys.stdin.readline

arr = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    arr[0][i] = i
for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, j + 1):
            arr[i][j] += arr[i - 1][k]
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n])