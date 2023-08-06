import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().split()
    a, b = list(a), list(b)
    if len(a) == len(b):
        for i in a:
            if i in b:
                b.remove(i)
        if len(b):
            print('Impossible')
        else:
            print('Possible')
    else:
        print('Impossible')