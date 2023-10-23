import sys
input = sys.stdin.readline
from collections import deque


def bfs(node):
    que = deque()
    que.append(node)
    visited = [-1] * (n + 1)
    visited[node] = 0

    while que:
        now = que.popleft()
        for next, cost in arr[now]:
            if visited[next] == -1:
                que.append(next)
                visited[next] = visited[now] + cost

    return visited


n = int(input())
arr = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    n1, n2, cost = map(int, input().split())
    arr[n1].append((n2, cost))
    arr[n2].append((n1, cost))


first_visited = bfs(1)
max_val = 0
max_idx = 0
for i in range(1, n + 1):
    if max_val < first_visited[i]:
        max_val = first_visited[i]
        max_idx = i

result_visited = bfs(max_idx)

print(max(result_visited))

