import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] + list(map(int, input().split()))

arr = [0] * (n + 1)

for _ in range(m):
    i, w = map(int, input().split())
    
    arr[i] += w
    
for i in range(2, n + 1):
    arr[i] += arr[parent[i]]

print(*arr[1:])