N = input()
number = list(map(int, input().split()))
line = []
n = 1
for i in number:
    if i == 0:
        line.append(n)
    else:
        line.insert(n - 1 - i, n)
    n += 1
print(*line)