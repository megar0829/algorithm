import sys
input = sys.stdin.readline
from copy import deepcopy


def dfs(start):
    n = start
    visited = [0] * (N + 1)
    visited[n] = 1
    stack = []
    stack.append(n)
    result = []
    result.append(n)
    while stack:
        for w in range(len(arr[n])):
            if visited[arr[n][w]] == 0:
                stack.append(n)
                n = arr[n].pop(w)
                visited[n] = 1
                result.append(n)
                break
        else:
            if stack:
                n = stack.pop()
    return result


def bfs(start):
    visited = [0] * (N + 1)
    visited[start] = 1
    que = []
    que.append(start)
    result = []
    while que:
        t = que.pop(0)
        result.append(t)
        for w in arr1[t]:
            if visited[w] == 0:
                que.append(w)
                visited[w] = 1
    return result


N, M, V = list(map(int, input().split()))
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for i in range(1, N + 1):
    arr[i].sort()

arr1 = deepcopy(arr)

print(*dfs(V))
print(*bfs(V))
