A, B, C = list(map(int, input().split()))
D = int(input())
C += D
while C >= 60:
    C -= 60
    B += 1
    if B == 60:
        A += 1
        B -= 60
    if A == 24:
        A -= 24
print(A, B, C)