import sys
input = sys.stdin.readline
import heapq

N = int(input())

pq = []

for _ in range(N):
    num = int(input())
    
    heapq.heappush(pq, num)

if N == 1:
    print(0)

else:
    ans = 0

    while pq:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        
        ans += (a + b)
        
        if not pq:
            break
        
        heapq.heappush(pq, a + b)

    print(ans)