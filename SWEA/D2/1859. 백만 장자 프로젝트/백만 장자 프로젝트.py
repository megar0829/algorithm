T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    max_val = 0
    for i in range(N - 1, -1, -1):
        if max_val <= arr[i]:
            max_val = arr[i]
        else:
            result += max_val - arr[i]
    print(f'#{tc} {result}')