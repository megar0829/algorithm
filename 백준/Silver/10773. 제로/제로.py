K = int(input())
lst = []
for i in range(1, K+1):
    number = int(input())
    if number != 0:
        lst.append(number)
    else:
        lst.pop()
print(sum(lst))