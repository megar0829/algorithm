K = int(input())
for _ in range(K):
    P, M = map(int ,input().split())
    chair = list(range(1, M + 1))
    cnt = 0
    for i in range(P):
        want_chair = int(input())
        if want_chair in chair:
            chair.pop(chair.index(want_chair))
        else:
            cnt += 1
    print(cnt)