N = int(input())
fx = input()
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arr = [int(input()) for _ in range(N)]
stack = [0] * len(fx)
top = -1
for i in fx:
    if i not in '+-*/':
        top += 1
        stack[top] = arr[alp.index(i)]
    else:
        op2 = stack[top]
        top -= 1
        op1 = stack[top]
        top -= 1
        if i == '+':
            top += 1
            stack[top] = op1 + op2
        elif i == '-':
            top += 1
            stack[top] = op1 - op2
        elif i == '*':
            top += 1
            stack[top] = op1 * op2
        elif i == '/':
            top += 1
            stack[top] = op1 / op2
print(f'{stack[top]:.2f}')