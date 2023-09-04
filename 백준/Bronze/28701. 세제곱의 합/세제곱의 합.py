N = int(input())
first = 0
second = 0
for i in range(1, N + 1):
    first += i
    second += i ** 3
print(first)
print(first ** 2)
print(second)