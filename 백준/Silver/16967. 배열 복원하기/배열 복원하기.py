import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H + X)]

A = [[0] * W for _ in range(H)]

result = [[0] * (W + Y) for _ in range(H + X)]

for i in range(H):
    if not B[i][-1]:
        A[i] = B[i][:W]
        result[i][:W] = A[i][:W]
    
    else:
        break

for i in range(W):
    if not B[-1][i]:
        for j in range(H):
            A[j][i] = B[j][i]
            result[j][i] = B[j][i]
    else:
        break
    
for i in range(X, X + H):
    for j in range(Y, Y + W):
        result[i][j] = B[i][j] - A[i - X][j - Y]
    
    if i < H:
        A[i] = result[i][:W]

for i in range(H):
    print(*result[i][:W])
