def line(arr):
    global top, num
    if stack[top] != num:
        return False
    else:
        top -= 1
        num += 1
    if top == -1:
        return True
    return line(arr)


N = int(input())
arr = list(map(int, input().split()))
stack = [0] * N
top = -1
num = 1
for i in range(N):
    if top == -1:
        if arr[i] == num:
            num += 1
        else:
            top += 1
            stack[top] = arr[i]
    else:
        while stack[top] == num:
            top -= 1
            num += 1
        if arr[i] == num:
            num += 1
        else:
            top += 1
            stack[top] = arr[i]

while stack[top] == num:
            top -= 1
            num += 1

if top != -1:
    if line(arr):
        print('Nice')
    else:
        print('Sad')
else:
    print('Nice')