import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    que = deque([a])
    visited[a] = 0
    
    while que:
        now = que.popleft()
        
        for next in arr[now]:
            if visited[next] == -1:
                que.append(next)
                visited[next] = visited[now] + 1


a, b = map(int, input().split())
N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    
    arr[x].append(y)
    arr[y].append(x)

visited = [-1] * (N + 1)

bfs()

print(visited[b])