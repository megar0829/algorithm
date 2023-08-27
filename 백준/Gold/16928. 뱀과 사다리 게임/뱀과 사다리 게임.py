from collections import deque


def bfs(start):
    visited = [0] * 101
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        t = que.popleft()
        
        if t == 100:
            return visited[t] - 1
        
        for i in range(1, 7):
            if 0 <= t + i < 101:
                if not visited[arr[t + i]]:
                    que.append(arr[t + i])
                    visited[arr[t + i]] = visited[t] + 1


N, M = map(int, input().split())

arr = list(range(101))
for _ in range(N):
    x, y = map(int, input().split())
    arr[x] = y
    
for _ in range(M):
    u, v = map(int, input().split())
    arr[u] = v

print(bfs(1))