import sys
input = sys.stdin.readline


N = int(input())

arr = [float(input()) for _ in range(N)]

for i in range(1, N):
    arr[i] = max(arr[i - 1] * arr[i], arr[i])

print("{:.3f}".format(max(arr)))