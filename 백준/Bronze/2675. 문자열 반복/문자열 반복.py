T = int(input())
for i in range(T):
    R, P = map(str, input().split())
    for j in range(len(P)):
        print(P[j]*int(R), end='')
    print('')