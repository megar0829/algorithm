T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = arr[0]
    for num in arr:
        if max_num < num:
            max_num = num
    matrix = [[0 for _ in range(max_num)] for i in range(N)]
    for i in range(N):
        for j in range(arr[i]):
            matrix[i][j] = 1
    height = []
    for i in range(max_num):
        cnt_zero = 0
        start = -1
        for j in range(N):
            if matrix[j][i] == 1 and start == -1:
                start = j
            elif matrix[j][i] == 0 and start != -1:
                cnt_zero += 1
        height.append(cnt_zero)
    if len(height):
        result = height[0]
        for i in range(max_num):
            if result < height[i]:
                result = height[i]
    else:
        result = 0

    print(f'#{tc} {result}')