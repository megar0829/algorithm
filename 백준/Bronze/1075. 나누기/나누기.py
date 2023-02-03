N = input()
F = int(input())
change_N = []
for i in range(len(N)):
    if i == len(N)-1 or i == len(N)-2:
        change_N.append('0')
    else:
        change_N.append(N[i])
N = ''
for j in change_N:
    N += j
cnt = 0
N = int(N)
while True:
    if N % F == 0:
        break
    else:
        N += 1
print(str(N)[len(str(N))-2:len(str(N))])