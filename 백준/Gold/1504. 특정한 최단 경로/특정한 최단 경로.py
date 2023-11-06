import sys
input = sys.stdin.readline
import heapq


def dijkstra(s, g):
    distance = [1e9] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, s))
    distance[s] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if distance[node] < dist:
            continue

        for next, cost in arr[node]:
            new_dist = dist + cost
            if distance[next] <= new_dist:
                continue

            distance[next] = new_dist
            heapq.heappush(pq, (new_dist, next))

    return distance[g]


N, E = map(int, input().split())

arr = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

result = 0

start, end = 1, N
v1, v2 = map(int, input().split())

root1 = 0
root1 += dijkstra(start, v1)
root1 += dijkstra(v1, v2)
root1 += dijkstra(v2, end)

root2 = 0
root2 += dijkstra(start, v2)
root2 += dijkstra(v2, v1)
root2 += dijkstra(v1, end)

result = min(root1, root2)

if result >= 1e9:
    print(-1)
else:
    print(result)