import heapq
import sys
N = int(sys.stdin.readline().strip())
heap = []
for i in range(N):
    numbers = int(sys.stdin.readline().strip())
    if numbers != 0:
        heapq.heappush(heap, (abs(numbers), numbers))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
