K, N, M = list(map(int, input().split()))
price = (K * N) - M
if price <= 0:
    print(0)
else:
    print(price)