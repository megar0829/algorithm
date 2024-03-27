import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

ans = 2e9

left, right = 0, 0

while True:
    if left > right:
        break
    
    if right == N:
        break
    
    gap = arr[right] - arr[left]
    
    if gap >= M:
        ans = min(ans, gap)
        left += 1

    else:
        right += 1
        
print(ans)