def distance(x, y, r):
    a = (r - x) ** 2
    b = (r - y) ** 2
    return (a + b) ** 0.5


T = int(input())
for tc in range(1, T + 1):
    r = int(input())
    arr = [[0] * ((2 * r) + 1) for _ in range((2 * r) + 1)]
    result = 0
    for i in range((2 * r) + 1):
        for j in range((2 * r) + 1):
            if distance(i, j, r) <= r:
                result += 1
    print(f'#{tc} {result}')