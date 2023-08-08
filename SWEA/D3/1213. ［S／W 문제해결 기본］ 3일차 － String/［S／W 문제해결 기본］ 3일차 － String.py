def bruteforce(pattern, target, i, j):
    global cnt
    n = len(pattern)
    m = len(target)
    while i < n and j < m:
        if pattern[i] != target[j]:
            j -= i
            i = -1
        i += 1
        j += 1
    if i == n:
        cnt += 1
        return bruteforce(pattern, target, 0, j)
    return cnt


for _ in range(10):
    tc = int(input())
    str1 = input()
    str2 = input()
    cnt = 0
    print(f'#{tc} {bruteforce(str1, str2, 0, 0)}')