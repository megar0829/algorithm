N, S = map(int, input().split())
arr = list(map(int, input().split())) + [0]

start = 0
end = 0
sum_val = arr[0]
l = 1
result = 1e9

while end < N:
    if sum_val < S:
        end += 1
        l += 1
        sum_val += arr[end]
    else:
        result = min(result, l)
        start += 1
        sum_val -= arr[start - 1]
        l -= 1
if result == 1e9:
    print(0)
else:
    print(result)