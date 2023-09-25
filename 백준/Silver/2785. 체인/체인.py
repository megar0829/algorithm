N = int(input())
arr = sorted(list(map(int, input().split())))
i = 0
cnt = 0

while len(arr) > 1:
    n = len(arr)
    arr[0] -= 1
    arr[n - 2] += arr[n - 1]
    arr.pop()
    cnt += 1
    if arr[0] == 0:
        arr.pop(0)
print(cnt)