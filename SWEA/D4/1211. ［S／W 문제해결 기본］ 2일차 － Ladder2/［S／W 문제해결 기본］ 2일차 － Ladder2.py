def right(arr, k, x1):
    global cnt
    if 0 <= k < 100 and 0 <= x1 < 100:
        if arr[k][x1] == 1:
            cnt += 1
            x1 += 1
            return right(arr, k, x1)
        else:
            x1 -= 1
            return x1
    else:
        x1 -= 1
        return x1


def left(arr, k, x2):
    global cnt
    if 0 <= k < 100 and 0 <= x2 < 100:
        if arr[k][x2] == 1:
            cnt += 1
            x2 -= 1
            return left(arr, k, x2)
        else:
            x2 += 1
            return x2
    else:
        x2 += 1
        return x2


def ladder(arr, x):
    global cnt
    for j in range(1, 100):
        if arr[j][x] == 1:
            cnt += 1
            if x == 0:
                if arr[j][x + 1] == 1:
                    x += 1
                    x = right(arr, j, x)
            elif x == 99:
                if arr[j][x - 1] == 1:
                    x -= 1
                    x = left(arr, j, x)
            else:
                if arr[j][x + 1] == 1:
                    x += 1
                    x = right(arr, j, x)
                elif arr[j][x - 1] == 1:
                    x -= 1
                    x = left(arr, j, x)
    return cnt

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    save_cnt = {}
    for i in range(100):
        cnt = 0
        if arr[0][i] == 1:  # 사다리의 첫 지점이 1 이면 출발
            cnt = ladder(arr, i)  # ladder 의 결과 도착했으면 True, 도착 못하면 False
            save_cnt[cnt] = i

    min_cnt = sorted(save_cnt.keys())[0]
    print(f'#{tc} {save_cnt[min_cnt]}')