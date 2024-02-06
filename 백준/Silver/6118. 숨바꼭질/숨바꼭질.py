from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    que = deque([1])
    visited[1] = 1
    
    while que:
        now = que.popleft()
        
        for next in arr[now]:
            if not visited[next]:
                que.append(next)
                visited[next] = visited[now] + 1


N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    
    arr[A].append(B)
    arr[B].append(A)
    
visited = [0] * (N + 1)    

bfs()

max_val = max(visited)

result_1 = visited.index(max_val)
result_2 = max_val - 1
result_3 = visited.count(max_val)

print(result_1, result_2, result_3)
