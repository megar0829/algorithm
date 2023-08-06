A, B, C = list(map(int, input().split()))
result1 = A * B / C
result2 = A / B * C

if result1 >= result2:
    print(int(result1))
else:
    print(int(result2))