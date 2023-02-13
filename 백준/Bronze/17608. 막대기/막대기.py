import sys
N = int(sys.stdin.readline())
h = [int(sys.stdin.readline()) for _ in range(N)]
rev_h = list(reversed(h))
cnt = 1
right = h[N-1]
for i in rev_h:
    if i > right:
        right = i
        cnt += 1
print(cnt)