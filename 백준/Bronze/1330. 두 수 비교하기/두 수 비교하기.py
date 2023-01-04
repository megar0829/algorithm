a, b = input().split()
A, B = int(a), int(b)
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')