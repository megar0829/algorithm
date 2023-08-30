import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    que = deque()
    visited[start] = 1
    que.append(start)
    while que:
        t = que.popleft()
        for w in arr[t]:
            if not visited[w]:
                visited[w] = -visited[t]
                que.append(w)
            else:
                if visited[w] == visited[t]:
                    return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)
    check = True
    visited = [0] * (V + 1)
    for i in range(1, V + 1):
        if not visited[i]:
            if not bfs(i):
                check = False
                break
    if check:
        print('YES')
    else:
        print('NO')