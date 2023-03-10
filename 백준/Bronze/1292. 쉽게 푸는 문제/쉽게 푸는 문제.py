A, B = map(int, input().split())
numbers = []
for i in range(1, 1000):
    for j in range(i):
        numbers.append(i)
print(sum(numbers[A-1:B]))