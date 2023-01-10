n = []
for i in range(1,31):
    n.append(int(i))
k = []
for j in range(28):
    k.append(int(input()))
for a in k:
    n.remove(int(a))
print(min(n))
print(max(n))