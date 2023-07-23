N = int(input())
times = list(map(int, input().split()))
M = 0
Y = 0
for i in times:
    Y += (i//30 + 1) * 10
    M += (i//60 + 1) * 15
if Y < M:
    print('Y', Y)
elif Y == M:
    print('Y', 'M', Y)
else:
    print('M', M)