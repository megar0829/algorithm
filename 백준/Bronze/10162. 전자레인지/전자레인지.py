N = int(input())
A = 0
B = 0
C = 0
if N % 10 != 0:
    print(-1)
else:
    while True:
        if N == 0:
            break
        if N >= 300:
            N -= 300
            A += 1
        elif N >= 60:
            N -= 60
            B += 1
        elif N >= 10:
            N -= 10
            C += 1
    print(A, B, C)