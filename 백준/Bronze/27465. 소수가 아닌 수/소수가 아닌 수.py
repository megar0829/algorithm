import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N+1, 10**9):
    numbers = list(range(1, i+1))
    cnt = 0
    for j in numbers:
        if i % j == 0:
            cnt +=1
    if cnt > 2:
        print(i)
        break