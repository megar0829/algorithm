from collections import deque


def bfs(N, K):
    que = deque()
    que.append(N)
    visited = [0] * (200001)
    visited[N] = 1
    while que:
        t = que.popleft()
        if t == K:
            return visited[t]
        for i in [t * 2, t - 1, t + 1]:
            if 0 <= i <= 100001:
                if visited[i] == 0:
                    if i == t * 2:
                        que.append(i)
                        visited[i] = visited[t]
                    else:
                        que.append(i)
                        visited[i] = visited[t] + 1


N, K = map(int, input().split())
if N == K:
    print(0)
else:
    print(bfs(N, K) - 1)