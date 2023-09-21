def binarySearch(start, end):
    if start > end:
        return end

    mid = (start + end) // 2

    tree = 0
    for i in range(N):
        if arr[i] > mid:
            tree += arr[i] - mid

    if tree >= M:
        return binarySearch(mid + 1, end)
    else:
        return binarySearch(start, mid - 1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
print(binarySearch(0, max(arr)))