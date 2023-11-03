import sys
input = sys.stdin.readline
import heapq


def dijkstra(start):
    global max_items
    pq = []
    distance = [1e9] * (n + 1)
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] > m:
            continue

        for next, length in arr[now]:
            new_dist = dist + length

            if distance[next] <= new_dist:
                continue

            distance[next] = new_dist
            heapq.heappush(pq, (new_dist, next))

    save_items = 0

    for node in range(1, n + 1):
        if distance[node] <= m:
            save_items += items[node - 1]

    max_items = max(max_items, save_items)


n, m, r = map(int, input().split())
items = list(map(int, input().split()))

arr = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    arr[a].append((b, l))
    arr[b].append((a, l))

max_items = 0

for i in range(1, n + 1):
    dijkstra(i)

print(max_items)