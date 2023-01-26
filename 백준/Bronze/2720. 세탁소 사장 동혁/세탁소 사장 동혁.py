T = int(input())
lst = [25, 10, 5 ,1]
for i in range(T):
    C = int(input())
    money = []
    n = 0
    cnt = 0
    while C != 0:
        if C >= lst[n]:
            C = C - lst[n]
            cnt += 1
        else:
            money.append(cnt)
            n += 1
            cnt = 0
    money.append(cnt)
    while len(money) < 4:
        money.append(0)
    print(*money)