import sys
input = sys.stdin.readline

N = int(input())
arr = {}
result = 0
for _ in range(N):
    name = input().strip('\n')
    if name == 'ENTER':
        result += len(arr.keys())
        arr = {}
    else:
        arr.setdefault(name, 0)
        arr[name] = 1

if arr:
    result += len(arr.keys())

print(result)