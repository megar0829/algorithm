T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            arr[i] += 1
    P = int(input())
    result = [0] * P
    for i in range(P):
        result[i] = arr[int(input())]
    print(f'#{tc}', *result)