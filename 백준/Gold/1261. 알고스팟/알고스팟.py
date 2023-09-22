import heapq

def dijkstra(s0, s1):
    pq = []
    heapq.heappush(pq, (0, s0, s1))
    visited[s0][s1] = 1
    while pq:
        cnt, i, j = heapq.heappop(pq)

        if (i, j) == (N - 1, M - 1):
            return cnt

        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj]:
                    heapq.heappush(pq, (cnt + 1, ni, nj))
                else:
                    heapq.heappush(pq, (cnt, ni, nj))


M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(dijkstra(0, 0))