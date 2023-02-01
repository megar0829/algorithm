N = int(input())
kms = ['4', '7']
for i in range(N, 3, -1):
    cnt = 0
    for j in str(i):
        if j not in kms:
            cnt += 1
    if cnt == 0:
        print(i)
        break