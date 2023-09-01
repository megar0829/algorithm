def subset(i, N, s):        # 합이 K 일때를 찾는 방법 2
    global cnt
    if i == N:
        if s == K:
            cnt += 1
            return
    else:
        bit[i] = 1
        subset(i + 1, N, s + arr[i])
        bit[i] = 0
        subset(i + 1, N, s)
    return


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    bit = [0] * N
    cnt = 0
    subset(0, N, 0)
    print(f'#{tc} {cnt}')