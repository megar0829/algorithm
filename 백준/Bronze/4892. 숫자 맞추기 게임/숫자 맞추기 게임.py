cnt = 0
while True:
    cnt += 1
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2:
        n2 = (n1 + 1) / 2
        result = 'odd'
    else:
        n2 = n1 / 2
        result = 'even'
    n3 = 3 * n2
    n4 = int(n3 // 9)
    print(f'{cnt}. {result} {n4}')