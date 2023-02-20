import sys
n = int(sys.stdin.readline())
n_1 = 0
n_2 = 1
lst = [0, 1]
for i in range(n-1):
    N = n_1 + n_2
    lst.append(N)
    n_1 = n_2
    n_2 = N
print(lst[n])