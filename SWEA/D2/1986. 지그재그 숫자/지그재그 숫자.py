T = int(input())
for i in range(1, T+1):
    N = int(input())
    sum_N = 0
    for j in range(1, N+1):
        if j % 2 == 0:
            sum_N -= j
        else:
            sum_N += j
    print(f'#{i} {sum_N}')