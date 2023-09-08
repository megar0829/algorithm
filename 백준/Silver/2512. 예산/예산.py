N = int(input())
arr = list(map(int, input().split()))
total_val = int(input())
sum_val = 0
max_val = 0
for i in range(N):
    sum_val += arr[i]
if sum_val <= total_val:
    print(max(arr))
else:
    max_val = sum(arr) // N
    sum_val = 0
    for i in range(N):
        if arr[i] <= max_val:
            sum_val += arr[i]
        else:
            sum_val += max_val
    if sum_val <= total_val:
        while True:
            sum_val = 0
            for i in range(N):
                if arr[i] <= max_val:
                    sum_val += arr[i]
                else:
                    sum_val += max_val
            if sum_val <= total_val:
                max_val += 1
            else:
                print(max_val - 1)
                break
    else:
        max_val -= 1
        while True:
            sum_val = 0
            for i in range(N):
                if arr[i] <= max_val:
                    sum_val += arr[i]
                else:
                    sum_val += max_val
            if sum_val <= total_val:
                print(max_val)
                break
            else:
                max_val -= 1