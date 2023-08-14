text = input()
result = ''
stack = [''] * len(text)
top = -1
check = 0
for i in text:
    if i == ' ':
        while top > -1:
            result += stack[top]
            top -= 1
        result += ' '
    elif i == '<':
        if top != -1:
            while top > -1:
                result += stack[top]
                top -= 1
        check = 1
        result += i
    elif i == '>':
        check = 0
        result += i
    else:
        if check:
            result += i
        else:
            top += 1
            stack[top] = i
if top != -1:
    while top > -1:
                result += stack[top]
                top -= 1
print(result)