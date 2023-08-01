T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = 0
    max_cnt = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
        else:
            if cnt != 0:
                cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')