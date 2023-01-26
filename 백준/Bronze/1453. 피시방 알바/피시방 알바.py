N = int(input())
lst = []
num = list(map(int, input().split()))
cnt = 0
for i in num:
    if i not in lst:
        lst.append(i)
    else:
        cnt += 1
print(cnt)