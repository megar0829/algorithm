import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = m - 1
node = 0
for i in range(1, n):
    if m == 2:
        print(i - 1, i)
    else:
        print(node, i)
        node += 1
        if cnt:
            cnt -= 1
            node -= 1