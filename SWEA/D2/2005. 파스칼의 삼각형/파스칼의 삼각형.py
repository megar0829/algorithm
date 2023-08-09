def memoization(input_arr, n):
    memo = [1]
    for i in range(n - 1):
        memo += [input_arr[n - 1][i] + input_arr[n - 1][i + 1]]
    memo += [1]
    return memo


arr = [[0]] * 10
arr[0] = [1]
arr[1] = [1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    if N > 2:
        for i in range(2, N):
            if arr[i] == [0]:
                arr[i] = memoization(arr, i)
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])