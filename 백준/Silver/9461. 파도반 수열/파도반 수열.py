arr = [1, 1, 1, 2, 2] + [0] * 95
for i in range(5, 100):
    arr[i] = arr[i - 5] + arr[i - 1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(arr[N - 1])