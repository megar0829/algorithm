import sys
input = sys.stdin.readline

a, b, c = list(map(int, input().split()))
parking = [0 for _ in range(101)]
for _ in range(3):
    x, y = map(int, input().split())
    for i in range(x, y):
        parking[i] += 1
price = 0
for i in parking:
    if i == 1:
        price += a
    elif i == 2:
        price += 2 * b
    elif i == 3:
        price += 3 * c
print(price)