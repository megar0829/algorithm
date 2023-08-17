T = int(input())
for tc in range(1, T + 1):
    # N : 손님의 수,  M, K : K 개의 붕어빵을 만드는 시간 M
    N, M, K = list(map(int, input().split()))
    # 손님의 도착 시간
    arr = sorted(list(map(int, input().split())))
    check = True
    bread = 0
    front = 0
    for i in range(11112):
        if not check or front >= N:
            break
        if i == 0:
            if i == arr[front]:
                if bread == 0:
                    check = False
                    break
        else:
            if i % M == 0:
                bread += K
            if i == arr[front]:
                if bread == 0:
                    check = False
                    break
                else:
                    while i == arr[front]:
                        if bread == 0:
                            check = False
                            break
                        bread -= 1
                        front += 1
                        if front >= N:
                            break
    if check:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')