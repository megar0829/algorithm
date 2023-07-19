T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    zero_cnt = 0
    for i in range(N, M + 1):
        if '0' in str(i):
            for j in str(i):
                if j == '0':
                    zero_cnt += 1
    print(zero_cnt)