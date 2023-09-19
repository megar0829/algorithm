import sys
input = sys.stdin.readline


def f(i, N, K):
    if i == K:
        result.add(tuple(sorted(p)))
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1
                f(i + 1, N, K)
                used[j] = 0


while True:
    ip = input().strip('\n')
    if ip == '0':
        break
    k, *arr = list(map(int, ip.split()))
    p = [0] * 6
    used = [0] * k
    result = set()
    f(0, k, 6)
    for rlt in sorted(list(result)):
        print(*rlt)
    print()