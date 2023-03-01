N = int(input())
for _ in range(N):
    mars = list(map(str, input().split()))
    result = float(mars.pop(0))    
    for i in mars:
        if i == '@':
            result *= 3
        elif i == '%':
            result += 5
        elif i == '#':
            result -= 7
    print(format(result, '.2f'))