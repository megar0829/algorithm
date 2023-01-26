for a in range(100000):
    M = int(input())
    if M == 0:
        break
    n = M*2
    a = [False, False] + [True]*(n-1)
    primes = []
    for i in range(2, int(n**0.5)+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    num = []
    for k in range(M+1, n+1):
        if a[k]:
            num.append(k)
    if M != 0:
        print(len(num))