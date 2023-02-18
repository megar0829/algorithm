import sys
N = int(sys.stdin.readline())
non_sum = 0
for i in range(N//2, N+1):
    sum_number = i
    save = i
    for j in range(len(str(i))):
        sum_number += i%10
        i = i // 10
    if sum_number == N:
        non_sum = save
        print(save)
        break    
if non_sum == 0:
    print(0)