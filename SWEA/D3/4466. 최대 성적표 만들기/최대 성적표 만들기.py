T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    result = 0
    for i in range(K):
        result += arr.pop()
    
    print(f'#{tc} {result}')