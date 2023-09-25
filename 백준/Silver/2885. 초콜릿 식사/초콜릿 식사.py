K = int(input())

i = 0
while True:
    if K <= 2 ** i:
        c = 2 ** i
        break
    i += 1

if c == K:
    print(c, 0)
else:
    sum_c = 0
    save_c = c
    cnt = 0
    while True:
        if sum_c == K:
            break
        save_c //= 2
        if sum_c + save_c <= K:
            sum_c += save_c
        cnt += 1
    print(c, cnt)
