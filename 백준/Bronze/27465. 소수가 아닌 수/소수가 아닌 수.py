import sys
import random
N = int(sys.stdin.readline())
lst = []
for i in range(N+1, 100*N):
    numbers = list(range(1, i+1))
    cnt = 0
    for j in numbers:
        if i % j == 0:
            cnt +=1
    if cnt > 2:
        lst.append(i)
print(random.choice(lst))