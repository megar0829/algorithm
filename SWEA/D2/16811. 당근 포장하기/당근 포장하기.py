T = int(input())
for tc in range(1, T + 1):
    N = int(input())            # 수확한 당근의 개수
    arr = list(map(int, input().split()))

    arr.sort()                  # 당근을 크기순으로 정렬
    min_v = 1000                # 포장별 최소 개수 차이
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            # 같은 크기 사이에 경계를 두면 안됨
            if arr[i] != arr[i + 1] and arr[j] != arr[j + 1]:
                small = i + 1       # 소 상자에 들어간 당근 개수
                mid = j - i         # 중 상자에 들어간 당근 개수
                large = N - 1 - j   # 대 상자에 들어간 당근 개수
                if small <= N // 2 and mid <= N // 2 and large <= N // 2:
                    save_v = max(small, mid, large) - min(small, mid, large)
                    if min_v > save_v:
                        min_v = save_v

    if min_v == 1000:
        min_v = -1

    print(f'#{tc} {min_v}')