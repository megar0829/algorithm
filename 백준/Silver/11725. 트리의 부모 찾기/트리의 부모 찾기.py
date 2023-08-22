import sys
input = sys.stdin.readline
from collections import deque


def bfs(n):
    result = [0] * (N + 1)
    visited = [0] * (N + 1)
    que = deque()
    que.append(n)
    visited[n] = 1
    while que:
        t = que.popleft()
        for w in arr[t]:
            if visited[w] == 0:
                que.append(w)
                result[w] = t
                visited[w] = visited[t] + 1
    return result


N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for i in bfs(1)[2:]:
    print(i)