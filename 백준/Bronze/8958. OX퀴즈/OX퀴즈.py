# import sys
# sys.stdin = open('input.txt', 'r')
T = int(input())
for i in range(T):
    M = input()
    cnt = 0
    cnt_sum = 0
    for j in range(len(M)):
        if M[j] == 'O':
            cnt += 1
            cnt_sum += cnt
        else:
            cnt = 0
    print(cnt_sum)