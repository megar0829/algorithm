def euclid(a, b):
    r = b % a
    if not r:
        return a
    return euclid(r, a)


D1, D2 = map(int, input().split())
arr = [[0] * D2 for _ in range(D2)]
cnt = 0

for i in range(D1, D2 + 1):
    for j in range(1, i + 1):
        r = euclid(i, j)
        
        x, y = i // r, j // r
        
        if not arr[x - 1][y - 1]:
            arr[x - 1][y - 1] = 1
            cnt += 1
print(cnt)