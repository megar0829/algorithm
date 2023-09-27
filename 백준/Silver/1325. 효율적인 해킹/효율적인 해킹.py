import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    global max_len
    que = deque()
    que.append(start)
    visited = [0] * (N + 1)
    visited[start] = 1
    cnt = 0
    while que:
        t = que.popleft()
        for next in graph[t]:
            if not visited[next]:
                visited[next] = visited[t] + 1
                que.append(next)
                cnt += 1
    max_len = max(max_len, cnt)
    return cnt, start


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    f, t = map(int, input().split())
    graph[t].append(f)

max_len = 0
result = []
for i in range(1, N + 1):
    result.append(bfs(i))

rlt = []
for c, idx in sorted(result, key=lambda x:(-x[0], x[1])):
    if c == max_len:
        rlt.append(idx)
    else:
        break
print(*rlt)