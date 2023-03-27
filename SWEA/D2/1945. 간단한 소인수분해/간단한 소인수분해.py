T = int(input())
for t in range(1, T+1):
    N = int(input())
    abcde = [2, 3, 5, 7, 11]
    numbers = [0, 0, 0, 0, 0]
    i = 0
    while True:
        if N % abcde[i] == 0:
            N = N / abcde[i]
            numbers[i] += 1
        i += 1
        if i > 4:
            i = 0
        if N == 1:
            break
    print(f'#{t}', *numbers)