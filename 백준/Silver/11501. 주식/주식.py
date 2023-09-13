import sys
input = sys.stdin.readline

T = int(input())
for _ in  range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sum_val = 0
    save_val = arr[N - 1]
    for i in range(N - 2, -1, -1):
        if arr[i] < save_val:
            sum_val += save_val - arr[i]
        elif arr[i] > save_val:
            save_val = arr[i]

    print(sum_val)