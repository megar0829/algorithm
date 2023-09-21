import heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, [0, start])
    distance[start[0]][start[1]] = 0
    while pq:
        dist, (i, j) = heapq.heappop(pq)

        if distance[i][j] < dist:
            continue

        for di, dj in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] > arr[i][j]:
                    diff = arr[ni][nj] - arr[i][j]
                else:
                    diff = 0
                cost = diff + 1
                new_cost = dist + cost

                if distance[ni][nj] <= new_cost:
                    continue
                distance[ni][nj] = new_cost
                heapq.heappush(pq, [new_cost, (ni, nj)])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1e9] * N for _ in range(N)]
    dijkstra((0, 0))
    print(f'#{tc} {distance[N - 1][N - 1]}')