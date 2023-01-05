total = int(input())
n = int(input())
squ = 1
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    squ = a * b
    sum += squ
if sum == total:
    print('Yes')
else:
    print('No')