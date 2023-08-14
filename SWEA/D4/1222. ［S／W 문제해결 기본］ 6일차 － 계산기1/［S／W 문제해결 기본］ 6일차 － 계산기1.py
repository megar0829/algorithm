for tc in range(1, 11):
    N = int(input())
    text = input()
    fx = ''
    cal_stack = [0] * (N // 2)
    top = -1

    for i in range(N):
        if text[i] not in '+-*/':
            fx += text[i]
        else:
            top += 1
            cal_stack[top] = text[i]
        if i == N - 1:
            while top > -1:
                fx += cal_stack[top]
                top -= 1

    stack = [0] * N
    top = -1
    for i in range(N):
        if fx[i] not in '+-*/':
            top += 1
            stack[top] = int(fx[i])
        else:
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            if fx[i] == '+':
                top += 1
                stack[top] = op1 + op2
            elif fx[i] == '-':
                top += 1
                stack[top] = op1 - op2
            elif fx[i] == '*':
                top += 1
                stack[top] = op1 * op2
            elif fx[i] == '/':
                top += 1
                stack[top] = op1 / op2
    print(f'#{tc} {stack[top]}')