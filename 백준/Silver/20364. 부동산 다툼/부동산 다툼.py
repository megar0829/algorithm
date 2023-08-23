import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = [0] * (N + 1)
for i in range(Q):
    node = int(input())
    check = 0
    n = node
    while n != 1:
        if arr[n] >= 1:
            check = n
        n //= 2    
    if check :
        print(check)
    else:
        arr[node] = 1
        print(0)