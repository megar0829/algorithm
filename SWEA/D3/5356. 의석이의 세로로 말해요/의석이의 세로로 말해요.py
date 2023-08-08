T = int(input())
for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]
    result = ''
    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])

    for i in range(max_len):
        for j in range(5):
            if i > len(arr[j]) - 1:
                pass
            else:
                result += arr[j][i]
    
    print(f'#{tc} {result}')