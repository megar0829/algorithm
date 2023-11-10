# 문제가 이해가 안됨

N = int(input())
arr = sorted(list(map(int, input().split())))

max_len = 0

if N < 3:
    max_len = N
else:
    for i in range(N - 2):
        for j in range(N - 1, -1, -1):
            if i + 1 > j:
                break
            if arr[i] + arr[i + 1] > arr[j]:
                max_len = max(max_len, j - i + 1)

print(max_len)