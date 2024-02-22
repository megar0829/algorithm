import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

idx = 0

stack = []

rlt = []

ans = ""
for num in range(1, n + 1):
    if num == arr[idx]:
        ans += "+-"
        rlt.append(num)
        idx += 1
        
        while stack and stack[-1] == arr[idx]:
            ans += "-"
            rlt.append(stack.pop())
            idx += 1
        
    else:
        ans += "+"
        stack.append(num)
        
if stack:
    print('NO')

else:
    for a in ans:
        print(a)