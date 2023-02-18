import sys
a, b = map(int, sys.stdin.readline().split())
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        print((a * b)//i)
        break