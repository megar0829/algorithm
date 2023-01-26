T = int(input())
s_lst = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(1, T+1):
    N, K = map(int, input().split())
    stu_dict = {}
    sort_dict = {}
    lst = []
    r_lst = []
    num_lst = list(range(N))
    for j in range(1, N+1):
        A, B, C = list(map(int, input().split()))
        stu_dict[j] = (0.35*A)+(0.45*B)+(0.2*C)
        lst.append((0.35*A)+(0.45*B)+(0.2*C))
        r_lst = sorted(lst,reverse=True)
    for k in range(len(s_lst)):
        cnt = 0
        for n in num_lst:
            sort_dict[r_lst[num_lst.pop(0)]] = s_lst[k]
            cnt += 1
            if cnt == int(N/10):
                break
    print(f'#{i} {sort_dict[stu_dict[K]]}')  