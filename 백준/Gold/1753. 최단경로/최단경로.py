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


V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

distance = [1e9] * (V + 1)

dijkstra(K)

for dist in distance[1:]:
    if dist == 1e9:
        print('INF')
    else:
        print(dist)