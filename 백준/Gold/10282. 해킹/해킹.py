import sys
input = sys.stdin.readline
import heapq


def dijkstra(start):
    distance = [1e9] * (n + 1)
    distance[start] = 0
    
    pq = []
    
    heapq.heappush(pq, (0, start))
    
    while pq:
        cost, now = heapq.heappop(pq)
        
        for dist, next in graph[now]:
            new_cost = cost + dist
            
            if new_cost >= distance[next]:
                continue
            
            distance[next] = new_cost
            heapq.heappush(pq, (new_cost, next))
            
    cnt, sum_time = 0, 0
    
    for time in distance:
        if time != 1e9:
            cnt += 1
            sum_time = max(sum_time, time)
    
    return (cnt, sum_time)
    

T = int(input())

for tc in range(T):
    n, d, c = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        
        graph[b].append((s, a))

    print(*dijkstra(c))