kms = [[] for _ in range(11)]

kms[1] = [4, 7]

for i in range(2, 11):
    for k in '47':
        for num in kms[i - 1]:
            kms[i].append(int(k[:] + str(num)[:]))

A, B = map(int, input().split())

a = len(str(A))
b = len(str(B))

cnt = 0
for idx in range(a, b + 1):
    for num in kms[idx]:
        if A <= num <= B:
            cnt += 1
            
        elif B < num:
            break

print(cnt)