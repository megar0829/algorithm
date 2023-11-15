import sys
input = sys.stdin.readline
from collections import deque


def bfs(cutline, start):
    que = deque([(start, 1e9)])
    visited = [0] * (N + 1)
    visited[start] = 1

    while que:
        now, pre_cost = que.popleft()

        for next, cost in graph[now]:
            if not visited[next] and cost >= cutline:
                que.append((next, cost))
                visited[next] = min(pre_cost, cost)

    cnt = 0
    for i in range(1, N + 1):
        if i != start and visited[i] >= cutline:
            cnt += 1

    return cnt


N, Q = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())

    print(bfs(k, v))