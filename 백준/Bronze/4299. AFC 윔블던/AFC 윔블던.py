a, b = map(int, input().split())
x = (a + b) / 2
y = (a - b) / 2

if a < b:
    print(-1)
elif a == 0 and b == 0:
    print(0, 0)
elif a == 0:
    print(-1)
elif (a + b) % 2 != 0 or (a - b) % 2 != 0:
    print(-1)
else:
    print(int(x), int(y))