numbers = list(map(int ,input().split()))
numbers = sorted(numbers)
for i in range(1, 1000000):
    cnt = 0
    for j in numbers:
        if i % j == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break