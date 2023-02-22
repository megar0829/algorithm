N = int(input())
for i in range(0, N):
    result = ' '*(i) + '*' *(((2*N)-1)-(2*i))
    print(result)
for i in range(N-2, -1, -1):
    result = ' '*(i) + '*' *(((2*N)-1)-(2*i))
    print(result)