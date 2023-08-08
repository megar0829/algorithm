T = int(input())
for tc in range(1, T + 1):
    arr = input()
    n = len(arr)
    raser = 0
    stack = 0
    result = 0
    for i in range(n):
        if arr[i] == '(' and arr[i + 1] == ')':
            if stack == 0:
                pass
            else:
                raser += 1
                result += stack
        elif arr[i] == '(':
            stack += 1
            result += 1
        elif arr[i] == ')' and arr[i - 1] != '(':
            stack -= 1

    print(f'#{tc} {result}')