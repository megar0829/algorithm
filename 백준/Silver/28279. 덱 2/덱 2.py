from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = deque()
for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        arr.appendleft(order[1])
    elif order[0] == 2:
        arr.append(order[1])
    elif order[0] == 3:
        if len(arr):
            print(arr.popleft())
        else:
            print(-1)
    elif order[0] == 4:
        if len(arr):
            print(arr.pop())
        else:
            print(-1)
    elif order[0] == 5:
        print(len(arr))
    elif order[0] == 6:
        if len(arr):
            print(0)
        else:
            print(1)
    elif order[0] == 7:
        if len(arr):
            print(arr[0])
        else:
            print(-1)
    elif order[0] == 8:
        if len(arr):
            print(arr[-1])
        else:
            print(-1)
    