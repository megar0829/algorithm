import heapq

def dijkstra(s0, s1):
    pq = []
    heapq.heappush(pq, (0, s0, s1))
    visited[s0][s1] = 1
    while pq:
        cnt, i, j = heapq.heappop(pq)
        if (i, j) == (N - 1, N - 1):
            return cnt

        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj <N:
                if not visited[ni][nj]:
                    visited[ni][nj] = 1
                    if arr[ni][nj]:
                        heapq.heappush(pq, (cnt, ni, nj))
                    else:
                        heapq.heappush(pq, (cnt + 1, ni, nj))


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
print(dijkstra(0, 0))