T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input()))
    arr = [0] * 10
    for i in numbers:
        arr[i] += 1
    max_num = 0
    max_value = arr[0]
    for i in range(10):
        if max_value <= arr[i]:
            max_num = i
            max_value = arr[i]
    print(f'#{tc} {max_num} {max_value}')
