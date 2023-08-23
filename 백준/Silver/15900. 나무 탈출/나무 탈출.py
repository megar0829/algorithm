from collections import deque
import sys
input = sys.stdin.readline


def bfs(n):
    visited = [0] * (N + 1)
    que = deque()
    que.append(n)
    visited[n] = 1
    result = 0
    while que:
        t = que.popleft()
        leaf = True
        for w in arr[t]:
            if visited[w] == 0:
                que.append(w)
                visited[w] = visited[t] + 1
                leaf = False
        if leaf:
            result += visited[t] - 1 
    return result

N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
    
if bfs(1) % 2:
    print('Yes')
else:
    print('No')