import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  K = int(input())
  arr = list(map(int, input().split()))
  heapq.heapify(arr)
  result = 0

  while len(arr) > 1:
    sum_val = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.heappush(arr, sum_val)
    result += sum_val
  
  print(result)