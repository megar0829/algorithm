T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N - (M - 1)):
        for j in range(N - (M - 1)):
            sum_kill = 0
            for k in range(M):
                for l in range(M):
                    sum_kill += arr[i + k][j + l]
            if result < sum_kill:
                result = sum_kill
    print(f'#{tc} {result}')