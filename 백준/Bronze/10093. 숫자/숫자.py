A, B = map(int, input().split())
if A > B:
    integer = list(range(B+1, A))
    print(len(integer))
    print(*integer)
elif A < B:
    integer = list(range(A+1, B))
    print(len(integer))
    print(*integer)
elif A == B:
    print(0)