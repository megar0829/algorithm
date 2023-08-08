def password(arr, i, j):
    arr.pop(j)
    arr.pop(i)
    if i <= len(arr) - 1:
        if arr[i - 1] == arr[i]:
            return password(arr, i - 1, i)
    return arr, i


for tc in range(1, 11):
    n, arr = input().split()
    n = int(n)
    arr = list(map(int, arr))
    i = 0
    while True:
        if i >= len(arr) - 1:
            break
        if arr[i] == arr[i + 1]:
            arr, i = password(arr, i, i + 1)
        else:
            i += 1
    result = ''
    for i in range(len(arr)):
        result += str(arr[i])
    print(f'#{tc} {result}')