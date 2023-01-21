A, B, C = list(map(int, input().split()))
if B >= C:
    print(-1)
else:
    bep = (A // (C-B)) +1
    print(bep)