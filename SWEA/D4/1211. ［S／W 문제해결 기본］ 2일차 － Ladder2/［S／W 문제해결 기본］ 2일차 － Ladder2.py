# 사다리에서 오른쪽에 값이 있을 경우
# 1 이 끝날 때까지 오른쪽으로 이동하는 함수
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


# 사다리에서 왼쪽에 값이 있을 경우
# 1 이 끝날 때까지 왼쪽으로 이동하는 함수
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


# 시작점부터 탐색하며 왼쪽 오른쪽에서 1 을 만나면
# 방향에 맞게 함수를 호출하여 탐색하며 
# 이동 횟수를 세는 함수
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
    min_cnt = 1000
    min_idx = 0
    for i in range(100):
        cnt = 0
        if arr[0][i] == 1:  # 사다리의 첫 지점이 1 이면 출발
            save_cnt = ladder(arr, i)  # ladder 의 결과 도착했으면 True, 도착 못하면 False
            if min_cnt > save_cnt:
                min_cnt = save_cnt
                min_idx = i

    print(f'#{tc} {min_idx}')