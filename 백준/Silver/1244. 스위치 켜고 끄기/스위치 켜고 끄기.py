import sys
input = sys.stdin.readline


def swich(n):
    if n:
        return 0
    return 1


def male(arr, n):
    for i in range(n, N, n + 1):
        arr[i] = swich(arr[i])
    return arr


def female(arr, n):
    global N
    arr[n] = swich(arr[n])
    for i in range(1, N):
        if (i <= n and i < N - n) and arr[n - i] == arr[n + i]:
            arr[n - i], arr[n + i] = swich(arr[n - i]), swich(arr[n + i])
        else:
            return arr


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, num = map(int, input().split())
    if gender == 1:
        arr = male(arr, num - 1)
    elif gender == 2:
        arr = female(arr, num - 1)
if N > 20:
    for i in range(1, (N // 20) + 2):
        print(*arr[20 * (i - 1):20 * i])
else:
    print(*arr)