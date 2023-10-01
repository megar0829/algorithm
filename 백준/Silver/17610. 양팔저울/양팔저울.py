def dfs(idx, number):
    if idx == k:
        if 0 < number <= S:
            result.add(number)
        return
    dfs(idx + 1, number + arr[idx])
    dfs(idx + 1, number - arr[idx])
    dfs(idx + 1, number)


k = int(input())
arr = list(map(int, input().split()))
S = sum(arr)
numbers = [0] * (S + 1)
result = set()
dfs(0, 0)

for i in result:
    numbers[i] = 1

cnt = 0
for i in range(1, S):
    if not numbers[i]:
       cnt += 1
       
print(cnt)