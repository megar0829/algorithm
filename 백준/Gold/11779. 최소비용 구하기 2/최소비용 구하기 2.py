import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append((t, w))

start, end = map(int, input().split())

distance = [1e9] * (n + 1)
prev_node = [start] * (n + 1)

pq = []
heapq.heappush(pq, (0, start))
distance[start] = 0

while pq:
    cost, now = heapq.heappop(pq)

    if distance[now] >= cost:
        for next, dist in graph[now]:
            new_cost = cost + dist
            if distance[next] > new_cost:
                distance[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
                prev_node[next] = now

path = [end]
prev = end

while prev != start:
    prev = prev_node[prev]
    path.append(prev)

print(distance[end])
print(len(path))
print(*reversed(path))
