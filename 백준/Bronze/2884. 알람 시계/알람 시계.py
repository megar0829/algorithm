H, M = input().split()
m = int(M) - 45
h = int(H)
if m >= 0:
    print(h, m)
else:
    if h == 0:
        g = h-1
        s = 24 + g
        n = 60 + m        
        print(s, n)
    else:
        n = 60 + m
        g = h-1
        print(g, n)
    