import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K, L = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(K)]

arr = [[0] * L for _ in range(N)]

for i in range(N):
    for j in range(L):
        save_val = 0
        for k in range(M):
            save_val += A[i][k] * B[k][j]
        arr[i][j] = save_val

for i in range(N):
    print(*arr[i])