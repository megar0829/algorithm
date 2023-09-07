from math import ceil

N = int(input())
cnt = 0
for i in range(ceil(N/3), ceil(N/2)):
    cnt += (i + 1) - ceil((N - i)/2)
print(cnt)