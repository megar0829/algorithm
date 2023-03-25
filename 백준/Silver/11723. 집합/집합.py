import sys
M = int(sys.stdin.readline().rstrip())
S = set()
for _ in range(M):
    calculation = sys.stdin.readline().rstrip().split()
    if calculation[0] == 'add':
        S.add(int(calculation[1]))
    elif calculation[0] == 'remove':
        if int(calculation[1]) in S:
            S.discard(int(calculation[1]))
    elif calculation[0] == 'check':
        if int(calculation[1]) in S:
            print(1)
        else:  
            print(0)
    elif calculation[0] == 'toggle':
        if int(calculation[1]) in S:
            S.discard(int(calculation[1]))
        else:
            S.add(int(calculation[1]))
    elif calculation[0] == 'all':
        S = set(list(range(1, 21)))
    elif calculation[0] == 'empty':
        S = set() 