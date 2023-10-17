N = int(input())
arr = sorted(list(map(int, input().split())))

numbers = {}
for i in range(N):
    numbers.setdefault(arr[i], 0)
    numbers[arr[i]] += 1

result = 0
for i in range(N - 2):
    left, right = i + 1, N - 1
    while left < right:
        sum_val = arr[i] + arr[left] + arr[right]

        if sum_val > 0:
            right -= 1
        else:
            if sum_val == 0:
                if arr[left] == arr[right]:
                    result += right - left
                else:
                    result += numbers[arr[right]]
            left += 1

print(result)