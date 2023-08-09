arr  = sorted(list(input()), reverse=True)
n = len(arr)
if '0' not in arr:
    print(-1)
else:
    cnt = 0
    sum_arr = 0
    for i in range(n - 1, -1, -1):
        if arr[i] == '0':
            cnt += 1
        else:
            sum_arr += int(arr[i])
    if sum_arr % 3 != 0:
        print(-1)
    else:
        print(*arr, sep='')