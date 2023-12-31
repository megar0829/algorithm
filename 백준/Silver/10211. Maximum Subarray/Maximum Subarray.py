import sys
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(1, N):
        arr[i] = max(arr[i - 1] + arr[i], arr[i])
    
    print(max(arr))