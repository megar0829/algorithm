for _ in range(10):
    T = int(input())
    password = list(map(int, input().split()))
    minus = 1
    while True:
        password.append(password[0]-minus)
        password.pop(0)
        minus += 1
        if minus == 6:
            minus = 1
        if password[7] <= 0:
            password[7] = 0
            break
    print(f'#{T}', *password)
