from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = deque()
idx = []
for _ in range(N):
    text = input().split()
    if text[0] == '1':
        arr.append(text[1])
        idx.append(-1)
    elif text[0] == '2':
        arr.appendleft(text[1])
        idx.append(0)
    elif text[0] == '3':
        if len(idx):
            n = idx.pop()
            if n == 0:
                arr.popleft()
            elif n == -1:
                arr.pop()
if len(arr):
    print(*arr, sep='')
else:
    print(0)