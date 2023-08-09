n = int(input())
cnt_5 = n // 5
while True:
    save_n = n
    save_n -= cnt_5 * 5
    if save_n % 2 == 0:
        cnt_2 = save_n // 2
        result = cnt_5 + cnt_2
        break
    else:
        cnt_5 -= 1
    if cnt_5 < 0:
        result = -1
        break
print(result)