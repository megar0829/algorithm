from collections import deque


def bfs(N, e):
    que = deque()
    visited = [[0, []] for _ in range(N + 1)]
    que.append(N)
    visited[N][0] = 1
    visited[N][1].append(N)
    while que:
        t = que.popleft()
        if t == e:
            return visited[e]
        for k in [t // 3, t // 2, t - 1]:
            if (k == t // 3 and t % 3 == 0) \
                or (k == t // 2 and t % 2 == 0) \
                    or (k == t - 1):
                if 0 <= k:
                    if visited[k][0] == 0 \
                            or visited[k][0] > visited[t][0] + 1:
                        que.append(k)
                        visited[k][0] = visited[t][0] + 1
                        visited[k][1] = visited[t][1][:]
                        visited[k][1].append(k)


N = int(input())
result = [N]
cnt = 0
visited_N = bfs(N, 1)
print(visited_N[0] - 1)
print(*visited_N[1])