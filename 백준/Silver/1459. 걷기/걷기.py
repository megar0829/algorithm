X, Y, W, S = map(int, input().split())

# Case 1. 수직 & 수평으로만 이동할 경우
dist1 = (X + Y) * W

# Case 2-1. 대각선으로만 이동 후 수직 or 수평으로 1번 이동할 경우
if (X + Y) % 2:
    dist2 = (max(X, Y) - 1) * S + W
# Case 2-2. 대각선으로만 이동할 경우
else:
    dist2 = (max(X, Y)) * S

# Case 3. 수징 & 수평 & 대각선으로 이동할 경우
dist3 = min(X, Y) * S + abs(X - Y) * W

print(min(dist1, dist2, dist3))