N = int(input())
result = 0
for _ in range(N):
    text = input()
    n = len(text)
    stack = [0] * n
    top = -1
    for i in range(n):
        if i == 0 or text[i] != stack[top]:
            top += 1
            stack[top] = text[i]
        else:
            top -= 1
    if top == -1:
        result += 1
print(result)