n = int(input())
n_0 = 0
n_1 = 1
for i in range(n-1):
    N = n_0 + n_1
    n_0 = n_1
    n_1 = N
if n == 1:
    N = n_1
print(N)