N = int(input())
ball = 1
for _ in range(N):
    x, y = map(int, input().split())
    if x == ball:
        ball = y
    elif y == ball:
        ball = x
    else:
        pass
print(ball)