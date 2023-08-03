def factorization(n):
    global a, b, c, d, e
    if n == 1:
        return a, b, c, d, e
    elif n % 2 == 0:
        n //= 2
        a += 1 
        return factorization(n)
    elif n % 3 == 0:
        n //= 3
        b += 1
        return factorization(n)
    elif n % 5 == 0:
        n //= 5
        c += 1
        return factorization(n)
    elif n % 7 == 0:
        n //= 7
        d += 1
        return factorization(n)
    elif n % 11 == 0:
        n //= 11
        e += 1
        return factorization(n)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    print(f'#{tc}', *factorization(N))