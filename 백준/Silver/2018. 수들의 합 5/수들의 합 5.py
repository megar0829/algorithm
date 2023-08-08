n = int(input())
cnt = sum_n = start = end = 1
while True:
    if start >= n // 2 + 1:
        break
    if sum_n == n:
        cnt += 1
        end += 1
        sum_n += end
    elif sum_n > n:
        sum_n -= start
        start += 1
    else:
        end += 1
        sum_n += end
print(cnt)