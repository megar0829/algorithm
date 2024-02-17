import sys
input = sys.stdin.readline

N, M = map(int, input().split())
train = ['0' * 20 for _ in range(N + 1)]

for _ in range(M):
    num, *ordered = list(map(int, input().split()))

    if num == 1:
        train[ordered[0]] = train[ordered[0]][:ordered[1] - 1] + '1' + train[ordered[0]][ordered[1]:]

    elif num == 2:
        train[ordered[0]] = train[ordered[0]][:ordered[1] - 1] + '0' + train[ordered[0]][ordered[1]:]

    elif num == 3:
        train[ordered[0]] = '0' + train[ordered[0]][:19]

    elif num == 4:
        train[ordered[0]] = train[ordered[0]][1:] + '0'

print(len(set(train[1:])))