import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
if n == 0:
    print(0)
else:
    difficulty = deque(sorted([int(input()) for _ in range(n)]))
    cut = round(n * 0.15 + 0.000000001)
    for i in range(cut):
        difficulty.pop()
        difficulty.popleft()
    print(round(sum(difficulty)/len(difficulty) + 0.000000001))