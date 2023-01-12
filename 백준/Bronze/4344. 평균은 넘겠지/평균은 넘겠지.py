# import sys
# sys.stdin = open('input.txt', 'r')
C = int(input())
for i in range(C):
    N = list(map(int, input().split()))
    n = N[0]
    N.pop(0)
    cnt = 0
    N_avr = sum(N) / n
    for j in N:
        if j > N_avr:
            cnt += 1
    percent = (cnt / n)* 100
    print('%0.3f%%'%percent)    
