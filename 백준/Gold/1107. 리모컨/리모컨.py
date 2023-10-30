N = int(input())
M = int(input())

if not M:
    print(min(len(str(N)), abs(100 - N)))
else:
    arr = list(map(int, input().split()))

    if N == 100:
        print(0)
    else:
        cnt = abs(N - 100)

        # 모든 숫자를 작은 순으로 탐색하며 리모컨으로 누를 수 있는 수라면 값 찾기

        n = len(str(N))
        for i in range(1000001):
            for j in str(i):
                if int(j) in arr:
                    break
            else:
                cnt = min(cnt, len(str(i)) + abs(N - i))

        print(cnt)
