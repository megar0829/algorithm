def divide(a, b, c):
    if b == 1:
        return a % C
    else:
        r = divide(a, b // 2, c) ** 2
        if b % 2 == 0:
            return r % c
        else:
            return (r * a) % c


A, B, C = map(int, input().split())
print(divide(A, B, C))