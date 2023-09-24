import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    distance = [1e9] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    
    while pq:
        dist, now = heapq.heappop(pq)
        
        if distance[now] >= dist:
            for node, cost in graph[now]:
                new_cost = dist + cost
                
                if distance[node] > new_cost:
                    distance[node] = new_cost
                    heapq.heappush(pq, (new_cost, node))
    if start != X:
            return distance[X]
    return distance


N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])


node_to_x = [0] * (N + 1)
for i in range(1, N + 1):
    if i != X:
        node_to_x[i] = dijkstra(i)

x_to_node = dijkstra(X)

result = []
for i in range(1, N + 1):
    if i != X:
        result.append(x_to_node[i] + node_to_x[i])
        
print(max(result))