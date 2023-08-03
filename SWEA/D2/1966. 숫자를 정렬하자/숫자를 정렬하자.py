T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        min_val = 50
        min_index = 0
        for j in range(i, N):
            if min_val > arr[j]:
                min_val = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f'#{tc}', *arr)