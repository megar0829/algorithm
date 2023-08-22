def cal(x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y


def postorder(n):
    if str(arr[n]) in '+-*/':
        postorder(ch1[n])
        postorder(ch2[n])
        arr[n] = cal(arr[ch1[n]], arr[n], arr[ch2[n]])


for tc in range(1, 11):
    N = int(input())
    arr = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for _ in range(N):
        data = list(input().split())
        if data[1] not in '+-*/':
            arr[int(data[0])] = int(data[1])
        else:
            arr[int(data[0])] = data[1]
        if len(data) == 4:
            ch1[int(data[0])] = int(data[2])
            ch2[int(data[0])] = int(data[3])
    postorder(1)
    print(f'#{tc} {int(arr[1])}')