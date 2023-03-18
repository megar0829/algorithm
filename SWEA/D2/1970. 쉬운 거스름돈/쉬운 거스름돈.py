T = int(input())
for t in range(1, T+1):
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    N = int(input())
    money = []
    cnt = 0
    for i in won:
        money.append(N // i)
        if money[cnt] != 0:
            N -= won[cnt] * money[cnt]
        cnt += 1 
    print(f'#{t}')
    print(*money)