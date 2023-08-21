import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
price = [int(input()) for _ in range(N)]
cars = [[int(input()), -1] for _ in range(M)]
result = 0
waiting = deque()
empty = deque(list(range(N)))
for _ in range(2 * M):
    i = int(input())
    if i > 0:
        if empty:
            idx = empty.popleft()
            cars[i - 1][1] = idx
            result += price[idx] * cars[i - 1][0]
        else:
            waiting.append(i - 1)
    else:
        empty.append(cars[(-1 * i) - 1][1])
        cars[(-1 * i) - 1][1] = -1
        empty = deque(sorted(empty))
        
    if waiting and empty:
        idx = empty.popleft()
        car = waiting.popleft()
        cars[car][1] = idx
        result += price[idx] * cars[car][0]

print(result)
