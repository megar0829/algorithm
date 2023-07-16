n = int(input())
x, y = 100, 100
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        pass
    elif a > b:
        y -= a
    elif a < b:
        x -= b
print(x)
print(y)