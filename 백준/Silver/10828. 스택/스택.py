import sys
input = sys.stdin.readline

N = int(input())
top = -1
arr = [0] * N
for _ in range(N):
    text = input().split()
    if text[0] == 'push':
        top += 1
        arr[top] = int(text[1])
    elif text[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(arr[top])
            top -= 1
    elif text[0] == 'size':
        print(top + 1)
    elif text[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif text[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(arr[top])