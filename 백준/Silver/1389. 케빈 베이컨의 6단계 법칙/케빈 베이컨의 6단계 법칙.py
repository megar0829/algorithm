import sys
input = sys.stdin.readline
from collections import deque


def bfs(n):
    visited = [0] * (N + 1)
    que = deque()
    que.append(n)
    visited[n] = 1
    save_val = 0
    while que:
        t = que.popleft()
        for w in arr[t]:
            if visited[w] == 0:
                que.append(w)
                visited[w] = visited[t] + 1
                save_val += visited[t]
            if save_val > min_val:
                return 100
    return save_val


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
min_val = 100
idx = 0
for i in range(1, N + 1):
    visited_val = bfs(i)
    if min_val > visited_val:
        min_val = visited_val
        idx = i
print(idx)