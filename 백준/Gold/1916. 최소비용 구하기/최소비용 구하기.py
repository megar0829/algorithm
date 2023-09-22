import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] >= dist:
            for next, cost in graph[now]:
                new_cost = dist + cost
                if distance[next] > new_cost:
                    distance[next] = new_cost
                    heapq.heappush(pq, (new_cost, next))


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
distance = [1e9] * (N + 1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

S, E = map(int, input().split())

dijkstra(S)
print(distance[E])