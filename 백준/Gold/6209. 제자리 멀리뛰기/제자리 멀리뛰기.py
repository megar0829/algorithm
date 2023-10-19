import sys
input = sys.stdin.readline


def binary_search(left, right):
    global min_dist
    if left > right:
        return

    mid = (left + right) // 2
    prev = 0
    cnt = 0
    for rock in arr:
        dist = rock - prev

        if dist < mid:
            cnt += 1
        else:
            prev = rock

    if cnt <= m:
        min_dist = mid
        return binary_search(mid + 1, right)

    else:
        return binary_search(left, mid - 1)


d, n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)] + [d])

min_dist = 0

binary_search(0, d)

print(min_dist)
