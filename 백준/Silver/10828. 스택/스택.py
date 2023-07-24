import sys
input = sys.stdin.readline

N = int(input())
lst_stack = []
for _ in range(N):
    order = list(map(str, input().split()))
    if order[0] == 'push':
        lst_stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(lst_stack) == 0:
            print(-1)
        else:
            print(lst_stack.pop())
    elif order[0] == 'size':
        print(len(lst_stack))
    elif order[0] == 'empty':
        if len(lst_stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(lst_stack) == 0:
            print(-1)
        else:
            print(lst_stack[-1])
