import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    print(N - 1)