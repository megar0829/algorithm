# 카운팅 정렬
def counting_sort(arr):
    counts = [0] * 101
    temp = [0] * 100
    for i in arr:
        counts[i] += 1
    for i in range(1, 101):
        counts[i] += counts[i - 1]
    for i in range(99, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]
    return temp

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = counting_sort(arr)
    for i in range(N):
        arr[0] += 1
        arr[-1] -= 1
        arr = counting_sort(arr)
    result = arr[-1] - arr[0]
    print(f'#{tc} {result}')