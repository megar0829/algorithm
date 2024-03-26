import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

lst = [0] * (N + 1)

for i in range(1, N):
    if arr[i - 1] > arr[i]:
        lst[i + 1] += 1
        
    lst[i + 1] += lst[i]

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    
    print(lst[y] - lst[x])