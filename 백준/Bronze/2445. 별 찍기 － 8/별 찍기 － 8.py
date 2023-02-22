N = int(input())
for i in range(1, N+1):
    result = '*'*(i) + ' ' *((2*N)-(2*i)) + '*'*(i)
    print(result)
for i in range(N-1, 0, -1):
    result = '*'*(i) + ' ' *((2*N)-(2*i)) + '*'*(i)
    print(result)