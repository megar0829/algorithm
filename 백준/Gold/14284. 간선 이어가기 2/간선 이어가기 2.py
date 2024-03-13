import sys
input = sys.stdin.readline
import heapq


def dijkstra():
    pq = []
    distance = [1e9] * (n + 1)
    distance[s] = 0
    heapq.heappush(pq, (0, s))
    
    while pq:
        cost, now = heapq.heappop(pq)
        
        for dist, next in graph[now]:
            new_cost = cost + dist
            
            if new_cost >= distance[next]:
                continue
            
            distance[next] = new_cost
            heapq.heappush(pq, (new_cost, next))

    print(distance[t])


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

s, t = map(int, input().split())

dijkstra()