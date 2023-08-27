def delta(i, j):
    result = arr[i][j]
    
    for k in range(N // 2 + 1, 0, -1):
        if k == N // 2 + 1:
            for n in range(1, k):
                result += arr[i - n][j]
                result += arr[i + n][j]
        else:
            if k == 1:
                result += arr[i][j - N // 2]
                result += arr[i][j + N // 2]
            else:
                for n in range(k):
                    if n == 0:
                        result += arr[i][j - (N // 2 + 1 - k)]
                        result += arr[i][j + (N // 2 + 1 - k)] 
                    else:
                        result += arr[i - n][j - (N // 2 + 1 - k)]
                        result += arr[i + n][j - (N // 2 + 1 - k)]
                        result += arr[i - n][j + (N // 2 + 1 - k)]
                        result += arr[i + n][j + (N // 2 + 1 - k)]
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {delta(N // 2, N // 2)}')