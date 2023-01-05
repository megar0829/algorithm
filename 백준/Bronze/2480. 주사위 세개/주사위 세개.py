a, b, c = input().split()
A, B, C = int(a), int(b), int(c)
sqe = [A, B, C]
prise = 0
if A == B == C:
    prise = 10000 + (A * 1000)
    print(prise)
elif A == B:
    prise = 1000 + (A * 100)
    print(prise) 
elif B == C: 
    prise = 1000 + (B * 100)
    print(prise)
elif C == A:
    prise = 1000 + (C * 100)
    print(prise)
else:
    prise = max(sqe) * 100
    print(prise)