P, K = map(int, input().split())
cnt = 0
p = 0
for i in range(2, K + 1):
    if P % i == 0:
        p = i
        cnt += 1
        break
if cnt == 1:
    if p == K:
        print('GOOD')
    else:
        print('BAD', p)
else:
    print('GOOD')