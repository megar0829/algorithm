N, K = map(int, input().split())
rooms = [0] * 12
cnt = 0
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 1:
        rooms[(2 * Y) - 2] += 1
    else:
        rooms[(2 * Y) - 1] += 1
for i in rooms:
    while i > 0:
        cnt += 1
        i = i - K
print(cnt)