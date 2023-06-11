num = 0
while True:
    num += 1
    L, P, V = list(map(int, input().split()))
    if L == P == V == 0:
        break
    day = 0
    cnt = V // P
    day += cnt * L
    V -= cnt * P
    if V >= L:
        day += L
    else:
        day += V 
    print(f'Case {num}: {day}')