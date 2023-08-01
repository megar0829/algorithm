for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    left_right = [-2, -1, 1, 2]
    result = 0
    for i in range(N):
        if arr[i] != 0:
            height = [0, 0, 0, 0]
            height[0] = arr[i] - arr[i - 2]
            height[1] = arr[i] - arr[i - 1]
            height[2] = arr[i] - arr[i + 1]
            height[3] = arr[i] - arr[i + 2]
            min_val = height[0]
            for j in range(3, 0, -1):
                for k in range(0, j):
                    if height[k] > height[k + 1]:
                        height[k], height[k + 1] = height[k + 1], height[k]
            if height[0] > 0:
                result += height[0]
    print(f'#{tc} {result}')