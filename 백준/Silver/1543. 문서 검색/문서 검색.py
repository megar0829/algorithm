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


target = input()
pattern = input()
cnt = 0
print(bruteforce(target, pattern, 0, 0))