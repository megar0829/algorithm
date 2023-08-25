for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 2 and cnt == 1:
                result += 1
                cnt = 0
            elif arr[j][i] == 1:
                cnt = 1
    print(f'#{tc} {result}')