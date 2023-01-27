import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for i in range(N):
    numbers = int(input())
    if numbers != 0:
        heapq.heappush(heap, numbers)
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)