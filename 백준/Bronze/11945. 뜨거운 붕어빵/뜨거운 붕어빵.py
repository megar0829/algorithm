N, M = map(int, input().split())
boonger = [input() for _ in range(N)]
for i in range(N):
    boonger[i] = boonger[i][::-1]
    print(boonger[i])