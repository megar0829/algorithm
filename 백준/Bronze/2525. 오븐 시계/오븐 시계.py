a, b = input().split()
A, B = int(a), int(b)
C = int(input())
B += C
if B < 60:
    print(A, B)
else:
    while B >= 60:
        B = B - 60
        A = A + 1
    if A >= 24:
        A = A - 24
        print(A, B)
    else:
        print(A, B)