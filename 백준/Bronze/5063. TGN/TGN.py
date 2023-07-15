N = int(input())
for _ in range(N):
    r, e, c = list(map(int ,input().split()))
    ad = e - c - r
    if ad > 0:
        print('advertise')
    elif ad == 0:
        print('does not matter')
    elif ad < 0:
        print('do not advertise')