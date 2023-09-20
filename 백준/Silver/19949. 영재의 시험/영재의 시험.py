def backTracking(i):
    global cnt
    if i == 10:
        save_cnt = 0
        for k in range(10):
            if lst[k] == arr[k]:
                save_cnt += 1
        if save_cnt >= 5:
            cnt += 1
        return
    else:
        for j in range(1, 6):
            if i > 1 and lst[i - 2] == lst[i - 1] == j:
                continue
            else:
                lst[i] = j
                backTracking(i + 1)
                lst[i] = 0


arr = list(map(int, input().split()))
N = len(arr)
cnt = 0
lst = [0] * N
backTracking(0)

print(cnt)