n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
total = 0
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
start = 1
stack = [start]
visited[start] = True
while stack:
    cur = stack.pop()
    for adj in graph[cur]:
        if not visited[adj]:
            visited[adj] = True
            stack.append(adj)
            total += 1
print(total)