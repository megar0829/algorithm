# import sys
# sys.stdin = open('input.txt', 'r')

n = []
m = []
cnt = 0
for i in range(10):
    n.append(int(input())%42)
for j in n:
    if j not in m:
        m.append(j)
        cnt += 1
print(cnt)