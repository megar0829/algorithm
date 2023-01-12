# 새로운 불면증 치료법
T = int(input())
for x in range(1, T+1):
    N = int(input())
    N_lst = []
    N_str = []
    n = 0 
    while sorted(N_lst) != list(range(0,10)):
        n += 1
        N_str.append(str(N*n))
        for i in str(N*n):
            if int(i) not in N_lst:
                N_lst.append(int(i))
    print(f'#{x} {N*n}')