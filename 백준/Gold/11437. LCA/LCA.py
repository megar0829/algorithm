import sys
input = sys.stdin.readline
from collections import deque


def bfs(root):
    visited = [0] * (N + 1)
    visited[root] = 1
    que = deque([root])

    while que:
        p = que.popleft()

        for c in arr[p]:
            if not visited[c]:
                que.append(c)
                visited[c] = p
                parent[c] = p
                depth[c] = depth[p] + 1


N = int(input())

arr = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

depth = [0] * (N + 1)
parent = [1] * (N + 1)

bfs(1)

M = int(input())
for _ in range(M):
    n1, n2 = map(int, input().split())

    while depth[n1] != depth[n2]:
        if depth[n1] < depth[n2]:
            n2 = parent[n2]
        else:
            n1 = parent[n1]

    while n1 != n2:
        n1 = parent[n1]
        n2 = parent[n2]
    print(n1)
