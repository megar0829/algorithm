import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
arr = deque()
while True:
    num = int(input())
    if num == -1:
        break
    if num == 0:
        arr.popleft()
    else:
        if len(arr) < N:
            arr.append(num)
if len(arr):
    print(*arr)
else:
    print('empty')