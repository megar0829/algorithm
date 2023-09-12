import sys
input = sys.stdin.readline

S = input()
q = int(input())
for _ in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    cnt = 0
    for i in range(l, r + 1):
        if S[i] == alpha:
            cnt += 1
    print(cnt)