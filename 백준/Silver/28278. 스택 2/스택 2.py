import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        arr.append(order[1])
    elif order[0] == 2:
        if len(arr):
            print(arr.pop())
        else:
            print(-1)
    elif order[0] == 3:
        print(len(arr))
    elif order[0] == 4:
        if len(arr):
            print(0)
        else:
            print(1)
    elif order[0] == 5:
        if len(arr):
            print(arr[-1])
        else:
            print(-1)