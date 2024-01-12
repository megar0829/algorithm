import sys
sys.setrecursionlimit(10 ** 9)
from collections import deque

    
def find_before_node(now):
    if now == N:
        result.append(now)
        return
    
    result.append(now)  
    find_before_node(visited[now][1])      
    

N, K = map(int, input().split())

que = deque([N])
visited = [(0, -1) for _ in range(200001)]
visited[N] = (1, N)

while que:
    now = que.popleft()
    
    for next in [(now * 2), (now - 1), (now + 1)]:
        if 0 <= next < 200001:
            if not visited[next][0] \
                or visited[next][0] > visited[now][0] + 1:
                que.append(next)
                visited[next] = (visited[now][0] + 1, now)

result = []

find_before_node(K)

print(visited[K][0] - 1)
print(*list(reversed(result)))