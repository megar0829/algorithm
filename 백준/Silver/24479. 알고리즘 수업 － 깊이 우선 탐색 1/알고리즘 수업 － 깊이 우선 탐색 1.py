import sys
input = sys.stdin.readline


def dfs(n):
    stack = [0] * N
    top = -1
    cnt = 1
    visited[n] = cnt
    while True:
        for w in range(len(arr[n])):
            if len(arr[n]) and visited[arr[n][w]] == 0:
                top += 1
                stack[top] = n
                n = arr[n].pop(w)
                cnt += 1
                visited[n] = cnt
                break
        else:
            if top != -1:
                n = stack[top]
                top -= 1
            else:
                return


N, M, R = list(map(int, input().split()))
arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    v, w = map(int, input().split())
    arr[v].append(w)
    arr[w].append(v)
for i in range(1, N + 1):
    arr[i].sort()

dfs(R)
for i in range(1, N + 1):
    print(visited[i])