N = int(input())
S = list(map(int, input().split()))
sum = 0
cnt = 0
for i in range(N):
    if S[i] == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)