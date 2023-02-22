N = int(input())
for i in range(N-1, -1, -1):
    result = ' '*(N-i-1) + '*'*(1+(2*i))
    print(result)