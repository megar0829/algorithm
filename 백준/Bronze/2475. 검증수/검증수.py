serial = list(map(int, input().split()))
sum_serial = 0
for i in serial:
    sum_serial += i**2
print(sum_serial % 10)