N, A, B = list(map(int, input().split()))
if N == B:
    if A > B:
        print('Subway')
    elif A == B:
        print('Anything')
    else:
        print('Bus')
else:
    if A > B:
        print('Subway')
    elif A == B:
        print('Anything')
    else:
        print('Bus')