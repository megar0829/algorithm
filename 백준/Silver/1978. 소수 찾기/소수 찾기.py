N = int(input())
n = list(map(int, input().split()))
lst = []
for i in n:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        lst.append(i)
print(len(lst))