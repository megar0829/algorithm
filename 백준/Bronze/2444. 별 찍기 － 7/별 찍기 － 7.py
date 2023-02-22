N = int(input())
for i in range(N):
    result = ' '*(N-i-1) + '*'*(1+(2*i))
    print(result)
for i in range(N-2, -1, -1):
    result = ' '*(N-i-1) + '*'*(1+(2*i))
    print(result)