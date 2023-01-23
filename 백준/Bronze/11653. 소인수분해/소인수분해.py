N = int(input())
num = 2
while N != 1:
    if N % num == 0:
        N = N / num
        print(num)
    else:
        num += 1