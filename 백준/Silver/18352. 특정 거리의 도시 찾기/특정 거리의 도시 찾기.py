import sys
input = sys.stdin.readline
from collections import deque


def bfs(start, num):
    visited = [0] * (N + 1)
    que = deque()
    que.append(start)
    visited[start] = 1
    result = []
    while que:
        t = que.popleft()
        for w in arr[t]:
            if visited[w] == 0:
                if visited[t] == num:
                    result.append(w)
                    visited[w] = visited[t] + 1
                else:
                    que.append(w)
                    visited[w] = visited[t] + 1

    if result:
        return sorted(result)
    result.append(-1)
    return result


N, M, K, X = list(map(int, input().split()))
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)

for i in bfs(X, K):
    print(i)