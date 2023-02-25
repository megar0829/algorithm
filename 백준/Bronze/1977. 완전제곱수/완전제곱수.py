M = int(input())
N = int(input())
squ = []
for i in range(M, N+1):
    if i**(1/2) % 1 == 0:
        squ.append(i)
if len(squ) == 0:
    print(-1)
else:
    print(sum(squ))
    print(squ[0])