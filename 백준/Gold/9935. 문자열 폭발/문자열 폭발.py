stack = []
text = input()
bomb = input()
n = len(bomb)

for i in text:
    stack.append(i)
    l = len(stack)
    if l >= n and i == bomb[-1]:
        save_text = ''
        for j in range(n - 1, -1, -1):
            save_text += stack[l - 1 - j]
        if save_text == bomb:
            for k in range(n):
                stack.pop()
if stack:
    print(*stack, sep='')
else:
    print('FRULA')