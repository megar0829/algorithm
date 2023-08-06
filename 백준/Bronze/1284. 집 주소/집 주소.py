while True:
    N = input()
    if N == '0':
        break
    result = 2 + len(N) -1
    for i in N:
        if i == '0':
            result += 4
        elif i == '1':
            result += 2
        else:
            result += 3
    print(result)