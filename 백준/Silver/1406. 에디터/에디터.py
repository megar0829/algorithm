import sys
input = sys.stdin.readline

text = list(input().strip('\n'))
M = int(input())
n = len(text)
stack = [0] * (M + n)
top = -1
cursor = n
for _ in range(M):
    order = input().strip('\n')
    if order == 'L':
        if text:
            top += 1
            stack[top] = text.pop()
    elif order == 'D':
        if top != -1:
            text.append(stack[top])
            top -= 1
    elif order == 'B':
        if text:
            text.pop()
    elif order[0] == 'P':
        text.append(order[2])
for i in range(top + 1):
    text.append(stack[top])
    top -= 1
print(*text, sep='')