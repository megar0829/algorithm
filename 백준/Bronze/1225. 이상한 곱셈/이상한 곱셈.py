import sys
A, B = sys.stdin.readline().split()
A = [int(_) for _ in A]
cnt = 0
for i in B:
    cnt += sum(A)*int(i)
print(cnt)