n = []
cnt = 0
for i in range(9):
    n.append(int(input()))
for j in n:
    cnt += 1
    if j == max(n):
        break
print(max(n))
print(cnt)