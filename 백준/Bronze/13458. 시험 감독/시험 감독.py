N = int(input())
A_i = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for i in A_i:
    i = i - B
    cnt += 1
    if i <= 0:
        pass
    else:
        cnt += i // C
        i = i % C
        if i > 0:
            cnt += 1
print(cnt)