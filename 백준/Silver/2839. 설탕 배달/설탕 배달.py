n = int(input())
cnt = 0
if n % 5 == 0:
    cnt = n // 5
    print(cnt)
else:
    while n % 5 != 0:
        n = n - 3
        cnt += 1
        if n % 5 == 0:
            print(cnt + n//5)
            break
        elif n == 0:
            print(cnt)
            break
        elif n < 0:
            print(-1)
            break