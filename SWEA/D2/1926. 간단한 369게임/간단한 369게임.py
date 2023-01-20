# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
lst_369 = []
for i in range(1, N+1):
    cnt_3 = str(i)
    cnt = 0
    for j in cnt_3:
        if j != '0':
            if int(j) % 3 == 0:
                cnt += 1
    if cnt != 0:
        lst_369.append('-'*cnt)
    else:
        lst_369.append(i)
print(*lst_369)