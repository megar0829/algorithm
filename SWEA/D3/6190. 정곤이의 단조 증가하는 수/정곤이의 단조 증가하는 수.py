def num(n):
    n = str(n)
    for i in range(1, len(n)):
        if n[i - 1] > n[i]:
            return False
    return True
        


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    result = []
    for i in range(N - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if num(arr[i] * arr[j]):
                result.append(arr[i] * arr[j])

    if result:
        print(f'#{tc} {sorted(result)[-1]}')
    else:
        print(f'#{tc} {-1}')