n = []
for i in range(7):
    n.append(int(input()))
m = []
for j in n:
    if j % 2 == 1:
        m.append(j)  
if len(m) > 0:
    print(sum(m))
    print(min(m))
else:
    print(-1)