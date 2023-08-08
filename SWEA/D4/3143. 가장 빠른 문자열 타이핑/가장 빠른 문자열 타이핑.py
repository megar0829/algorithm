def bruteforce(target, pattern, i, j):
    global cnt
    n = len(target)
    m = len(pattern)
    while i < n and j < m:
        if target[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == m:
        cnt += 1
        return bruteforce(target, pattern, i, 0)
    return cnt

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    cnt = 0
    check = bruteforce(A, B, 0, 0)
    result = len(A) - ((len(B) - 1) * check)
    print(f'#{tc} {result}')