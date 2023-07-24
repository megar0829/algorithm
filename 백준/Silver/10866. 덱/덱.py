import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
lst_deque = deque()
for _ in range(N):
    order = list(map(str, input().split()))
    if order[0] == 'push_front':
        lst_deque.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        lst_deque.append(int(order[1]))
    elif order[0] == 'pop_front':
        if len(lst_deque) == 0:
            print(-1)
        else:
            print(lst_deque.popleft())
    elif order[0] == 'pop_back':
        if len(lst_deque) == 0:
            print(-1)
        else:
            print(lst_deque.pop())
    elif order[0] == 'size':
        print(len(lst_deque))
    elif order[0] == 'empty':
        if len(lst_deque) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(lst_deque) == 0:
            print(-1)
        else:
            print(lst_deque[0])
    elif order[0] == 'back':
        if len(lst_deque) == 0:
            print(-1)
        else:
            print(lst_deque[-1])
