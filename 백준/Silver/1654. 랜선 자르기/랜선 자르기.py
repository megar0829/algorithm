import sys
input = sys.stdin.readline

def binarySearch(start, end):
    if start > end:
        return end

    mid = (start + end) // 2
    lan = 0
    for i in range(K):
        lan += arr[i] // mid

    if lan >= N:
        return binarySearch(mid + 1, end)
    else:
        return binarySearch(start, mid - 1)


K, N = map(int, input().split())
arr = sorted([int(input()) for _ in range(K)])
print(binarySearch(1, arr[K - 1]))