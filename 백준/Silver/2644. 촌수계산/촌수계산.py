import sys
input = sys.stdin.readline


def bfs(start, end):
    visited = [0] * (n + 1)
    que = []
    que.append(start)
    visited[start] = 1
    while que:
        t = que.pop(0)
        for w in arr[t]:
            if visited[w] == 0:
                que.append(w)
                visited[w] = visited[t] + 1
    if not visited[end]:
        return -1
    return visited[end] - 1


n = int(input())
x, y = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
    
print(bfs(x, y))