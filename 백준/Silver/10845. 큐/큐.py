import sys
input = sys.stdin.readline

N = int(input())
lst_queue = []
for _ in range(N):
    order = list(map(str, input().split()))
    if order[0] == 'push':
        lst_queue.append(int(order[1]))
    elif order[0] == 'pop':
        if len(lst_queue) == 0:
            print(-1)
        else:
            print(lst_queue.pop(0))
    elif order[0] == 'size':
        print(len(lst_queue))
    elif order[0] == 'empty':
        if len(lst_queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(lst_queue) == 0:
            print(-1)
        else:
            print(lst_queue[0])
    elif order[0] == 'back':
        if len(lst_queue) == 0:
            print(-1)
        else:
            print(lst_queue[-1])
