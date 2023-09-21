import sys
input = sys.stdin.readline
import heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for node, cost in graph[now]:
            new_cost = dist + cost

            if distance[node] <= new_cost:
                continue
            distance[node] = new_cost
            heapq.heappush(pq, (new_cost, node))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [1e9] * (N + 1)
for _ in range(M):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])
    graph[t].append([f, w])

dijkstra(1)
print(distance[N])

