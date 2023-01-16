N, X = map(int, input().split())
A = list(map(int, input().split()))
A_x =[]
for i in A:
    if i < X:
        A_x.append(i)
print(*A_x)