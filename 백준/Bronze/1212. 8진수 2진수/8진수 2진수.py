N = input()
dec = [0] * (len(N) * 3)
index = 0
if N == '0':
    print(0)
else:
    for i in N:
        i = int(i)
        if i >= 4:
            dec[index] = 1
            i = i - 4
            index += 1
        else:
            index += 1
            pass
        if i >= 2:
            dec[index] = 1
            i = i - 2
            index += 1
        else:
            index += 1
            pass
        if i > 0:
            dec[index] = 1
            index += 1
        else:
            index += 1
            pass
    while dec[0] == 0:
        dec.pop(0)
    print(*dec, sep='')