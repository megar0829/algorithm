arr = [0] * 10001
arr[1] = 1
arr[2] = 2
for i in range(3, 10001):
    cnt = 0
    for j in range(1, int((i ** 0.5)) + 1):
        if i % j == 0:
            cnt += 1
    arr[i] = cnt + arr[i - 1]

n = int(input())
print(arr[n])