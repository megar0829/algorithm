for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    result = 0
    for i in range(8):
        for j in range(8 - n + 1):
            row = 0
            col = 0
            for k in range(n // 2):
                if arr[i][j + k] != arr[i][j + (n - 1) - k]:
                    row += 1
                if arr[j + k][i] != arr[j + (n - 1) - k][i]:
                    col += 1
            if row == 0:
                result += 1
            if col == 0:
                result += 1
    print(f'#{tc} {result}')