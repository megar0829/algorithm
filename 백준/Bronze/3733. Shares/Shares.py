while True:
    try:
        N, S = map(int, input().split())
        if N + 1 > S:
            print(0)
        else:
            print(S // (N + 1))
    except EOFError:
        break