def Rev(x):
    x = str(x)
    x_rev = x[::-1]
    x = int(x_rev)
    return x

X, Y = input().split()
print(Rev(Rev(X)+Rev(Y)))