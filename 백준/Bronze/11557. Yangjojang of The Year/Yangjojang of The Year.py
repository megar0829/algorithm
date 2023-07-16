T = int(input())
for _ in range(T):
    N = int(input())
    drink = {}
    for i in range(N):
        S, L = input().split()
        drink[S] = int(L)
    first = max(drink.values())
    for k, v in drink.items():
        if v == first:
            print(k)
    