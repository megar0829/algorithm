from collections import deque


def bfs():
    que = deque([0])
    visited[0] = 1
    
    while que:
        now = que.popleft()
        
        if now == N - 1:
            break
        
        for val in range(arr[now], 0, -1):
            next = now + val
            
            if next < N and not visited[next]:
                que.append(next)
                visited[next] = visited[now] + 1
                
                
N = int(input())
arr = list(map(int, input().split()))
visited = [0] * N

bfs()

print(visited[N - 1] - 1)