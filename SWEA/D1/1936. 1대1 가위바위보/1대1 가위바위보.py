# import sys
# sys.stdin = open('input.txt', 'r')

A, B = list(map(int, input().split()))
if (A == 3) and (B == 2):
    print('A')
elif (A == 2) and (B == 1):
    print('A')
elif (A == 1) and (B == 3):
    print('A')
else:
    print('B')