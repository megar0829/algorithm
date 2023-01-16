N = int(input())
list_0 = []
list_1 = []
for i in range(N):
    A = int(input())
    if A == 1:
        list_1.append(A)
    else:
        list_0.append(A)
if len(list_0) > len(list_1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')