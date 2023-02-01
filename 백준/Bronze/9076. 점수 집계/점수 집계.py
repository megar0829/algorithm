T = int(input())
for i in range(T):
    N = list(map(int, input().split()))
    N.pop(N.index(max(N)))
    N.pop(N.index(min(N)))
    if max(N) - min(N) >= 4:
        print('KIN')
    else:
        print(sum(N))