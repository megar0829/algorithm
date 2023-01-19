sqr = 1
for i in range(3):
    i = int(input())
    sqr *= i
sqr_dict = {}
for j in range(10):
    sqr_dict[j] = str(sqr).count(str(j))
for value in sqr_dict:
    print(sqr_dict[value])
