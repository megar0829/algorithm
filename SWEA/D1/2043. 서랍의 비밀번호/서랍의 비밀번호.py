# 서랍의 비밀번호
P, K = map(int, input().split())
cnt = 1
while K != P:
    K += 1
    cnt += 1
print(cnt)