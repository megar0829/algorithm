for tc in range(1, 11):
    N = int(input())
    text = input()
    stack = [0] * N
    s = {'+':1, '*':2}
    top = -1
    arr = ''
    for i in range(N):
        if text[i] not in '+*':
            arr += text[i]
        else:
            if top == -1 or s[stack[top]] <= s[text[i]]:
                top += 1
                stack[top] = text[i]
            else:
                while top > -1 and s[stack[top]] >= s[text[i]]:
                    arr += stack[top]
                    top -= 1
                top += 1
                stack[top] = text[i]
    for i in range(top + 1):
        arr += stack[top]
        top -= 1
    stack = [0] * N
    top = -1
    for i in range(N):
        if arr[i] not in '+*':
            top += 1
            stack[top] = int(arr[i])
        else:
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            if arr[i] == '+':
                top += 1
                stack[top] = op1 + op2
            elif arr[i] == '*':
                top += 1
                stack[top] = op1 * op2
    print(f'#{tc} {stack[top]}')