n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in range(m):
    sum_val = arr[0] + arr[1]
    arr[0], arr[1] = sum_val, sum_val
    arr.sort()
print(sum(arr))