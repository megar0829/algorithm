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


N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]
distance = [1e9] * (D + 1)

# 만약 중간에 지름길이 없으면 계속 1 씩 증가할 수 있도록 모두 1 로 초기화
for i in range(D):
    graph[i].append((i + 1, 1))

for i in range(N):
    start, end, l = map(int, input().split())
    if end <= D:
        graph[start].append((end, l))

dijkstra(0)
print(distance[D])