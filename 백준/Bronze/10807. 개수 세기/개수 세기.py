N = int(input())
n = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in n:
    if i == v:
        cnt +=1
print(cnt)        