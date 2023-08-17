def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    return n * fibo(n - 1)


N = int(input())
print(fibo(N))