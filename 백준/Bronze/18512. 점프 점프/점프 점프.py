x, y, p1, p2 = list(map(int, input().split()))

x_p = [0] * 101
y_p = [0] * 101
x_p[0], y_p[0] = p1, p2
for i in range(1, 101):
    x_p[i] = x_p[i - 1] + x
    y_p[i] = y_p[i - 1] + y

result = 0
for i in range(100):
    for j in range(100):
        if x_p[i] < y_p[j]:
            break
        if x_p[i] == y_p[j]:
            result = x_p[i]
            break
    if result != 0:
        break
if result == 0:
    print(-1)
else:
    print(result)