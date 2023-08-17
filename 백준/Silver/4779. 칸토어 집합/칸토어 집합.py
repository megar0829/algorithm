def third(cnt, start, end):
    if cnt == 0:
        return

    val_3 = ((end + 1) - start) // 3
    third(cnt - 1, start, start + val_3 - 1)
    for i in range(start + val_3, start + (val_3 * 2)):
        arr[i] = ' '

    third(cnt - 1, start + val_3 * 2, start + (val_3 * 3) - 1)


while True:
    try:
        N = int(input())
        arr = ['-'] * (3 ** N)
        third(N, 0, (3 ** N) - 1)
        print(*arr, sep='')
    except :
        break