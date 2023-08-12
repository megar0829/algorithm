text = input()
n = len(text)
stick = 0
result = 0
for i in range(n - 1):
    if text[i] == '(' and text[i + 1] == ')':
        if stick != 0:
            result += stick
    elif text[i] == '(':
        stick += 1
        result += 1
    elif text[i] == ')' and text[i - 1] != '(':
        stick -= 1
print(result)