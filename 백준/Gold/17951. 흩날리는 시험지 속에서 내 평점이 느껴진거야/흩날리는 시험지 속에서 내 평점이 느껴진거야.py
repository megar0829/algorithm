# 모두 더한 값을 right로 지정하고 그 중간값을 찾으며 
# 그룹의 개수가 K 개를 만족하면 그때의 값을 저장

def binary_search(left, right):
    global ans
    if left > right:
        return

    mid = (left + right) // 2

    group = 0
    sum_val = 0
    for i in range(N):
        sum_val += arr[i]
        if sum_val >= mid:
            group += 1
            sum_val = 0

    if group < K:
        return binary_search(left, mid - 1)
    else:
        ans = mid
        return binary_search(mid + 1, right)


N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
binary_search(0, sum(arr))
print(ans)