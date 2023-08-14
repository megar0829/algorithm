text = input()
stack = [0] * len(text)
top = -1
result = 0
for i in text:
    if i == '(':
        top += 1
        stack[top] = i
    else:
        if top == -1:
            result += 1
        elif stack[top] == '(':
            top -= 1
if top != -1:
    result += top + 1
print(result)