import sys
input = sys.stdin.readline
import heapq


def dijkstra(s):
    distance = [1e9] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, s))
    distance[s] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        for next, cost in arr[now]:
            new_dist = dist + cost

            if distance[next] <= new_dist:
                continue

            distance[next] = new_dist
            heapq.heappush(pq, (new_dist, next))

    return distance


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    arr = [[] for _ in range(n + 1)]
    save_dist = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        arr[a].append((b, d))
        arr[b].append((a, d))
        if a == g and b == h:
            save_dist = d

    target = []
    for _ in range(t):
        x = int(input())
        target.append((x))

    start_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)

    result = []

    for goal in target:
        root1 = start_dist[goal]
        root2 = start_dist[g] + g_dist[h] + h_dist[goal]
        root3 = start_dist[h] + h_dist[g] + g_dist[goal]

        if root1 == root2 or root1 == root3:
            result.append(goal)

    print(*sorted(result))