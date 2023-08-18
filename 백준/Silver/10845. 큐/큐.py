import sys
input = sys.stdin.readline


def isEmpty():
    if rear == front:
        return 1
    return 0


N = int(input())
arr = [0] * N
front = rear = -1
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        rear += 1
        arr[rear] = int(order[1])
    elif order[0] == 'pop':
        if isEmpty():
            print(-1)
        else:
            front += 1
            print(arr[front])
    elif order[0] == 'size':
        print(rear - front)
    elif order[0] == 'empty':
        print(isEmpty())
    elif order[0] == 'front':
        if isEmpty():
            print(-1)
        else:
            print(arr[front + 1])
    elif order[0] == 'back':
        if isEmpty():
            print(-1)
        else:
            print(arr[rear])