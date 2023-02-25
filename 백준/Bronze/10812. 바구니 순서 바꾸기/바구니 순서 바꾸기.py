N, M = map(int, input().split())
basket = list(range(1, N+1))
copy_basket = list(range(1, N+1))
for _ in range(M):
    i, j, k = list(map(int, input().split()))
    for q in range(j - i + 1):
        if (k - 1 + q) < j:
            basket[i - 1 + q] = copy_basket[k - 1 + q]
        else:
            basket[i - 1 + q] = copy_basket[i - 1 + q - (j - k + 1)]
    for w in range(N):
        copy_basket[w] = basket[w]
print(*basket)