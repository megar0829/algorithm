n = int(input())
for _ in range(n):
    p = int(input())
    price, name = 0, ''
    for i in range(p):
        C, N = input().split()
        if int(C) > price:
            price = int(C)
            name = N
    print(name)