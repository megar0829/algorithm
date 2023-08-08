import sys
input = sys.stdin.readline

N = int(input())
result = 0
for _ in range(N):
    text = input()
    check = []
    cnt = 0
    for i in text:
        if i not in check:
            check.append(i)
        elif i in check and check[-1] == i:
            # check.append(i)
            pass
        else:
            cnt += 1
    if cnt == 0:
        result += 1
print(result)