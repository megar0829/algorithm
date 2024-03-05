from collections import deque

def bfs():
    que = deque([N])
    visited[N] = 0
    
    while que:
        now = que.popleft()
        
        if now == M:
            return
        
        for next in [
            now - 1, now + 1,\
            now - A, now + A,\
            now - B, now + B,\
            now * A, now * B
                    ]:
            
            if 0 <= next <= 100000 and visited[next] == -1:
                que.append(next)
                visited[next] = visited[now] + 1
    

A, B, N, M = map(int, input().split())

visited = [-1] * (100001)

bfs()

print(visited[M])