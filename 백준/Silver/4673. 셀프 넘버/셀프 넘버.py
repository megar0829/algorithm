def selfnumber(n):
    number = n
    while n != 0:
        number = number + (n % 10)
        n = n // 10
    return number
self_lst = []
for i in range(1,10000):
    self_lst.append(selfnumber(i))
    if i not in self_lst:
        print(i)