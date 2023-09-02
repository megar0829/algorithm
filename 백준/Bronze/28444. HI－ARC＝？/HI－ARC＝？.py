H, I, A, R, C = list(map(int, input().split()))
result = ''
first = H * I  
second = A * R * C
result = first - second
print(result)