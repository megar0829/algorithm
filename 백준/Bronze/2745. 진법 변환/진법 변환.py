N, B = map(str, input().split())
N = N[::-1]
B = int(B)
alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
for k in range(len(N)):
    result += alp.index(N[k]) * (B**k)
print(result)