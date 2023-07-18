T = int(input())
for _ in range(T):
    n = int(input())
    n_2_index = []
    n_2 = str(bin(n))[::-1]
    cnt = 0
    for i in n_2:
        if i == '1':
            n_2_index.append(cnt)
        cnt += 1
    print(*n_2_index)