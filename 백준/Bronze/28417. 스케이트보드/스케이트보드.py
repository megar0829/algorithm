import sys
input = sys.stdin.readline


N = int(input())
result = [0] * N
for t in range(N):
    a, b, *arr = list(map(int, input().split()))
    if a > b:
        top_run = a
    else:
        top_run = b

    # arr = bubble_sort_reverse(arr, 5)
    arr.sort(reverse=True)
    top_trick = arr[0] + arr[1]
    result[t] = top_run + top_trick

print(sorted(result, reverse=True)[0])