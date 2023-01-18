A = []
B = []
xy = []
for i in range(3):
    C, D = map(int, input().split())
    if C not in A:
        A.append(C)
    else:
        A.pop(A.index(C))
    if D not in B:
        B.append(D) 
    else:
        B.pop(B.index(D))
print(*A, *B)