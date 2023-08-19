def bfs(start, end):
    visited = [0] * (max_val)
    que = []
    que.append(start)
    while que:
        t = que.pop(0)
        if t == end:
            return visited[t]
        for i in [t - 1, t + 1, t * 2]:
            if 0 <= i < max_val and visited[i] == 0:
                que.append(i)
                visited[i] = visited[t] + 1
                

N, K = map(int, input().split())
max_val = 100001
print(bfs(N, K))