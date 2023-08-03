N = int(input())
arr = input()
cnt = 1
for i in arr:
    if i == 'S':
        cnt += 1
    elif i == 'L':
        cnt += 0.5
if int(cnt) < N:
    print(int(cnt))
else:
    print(N)