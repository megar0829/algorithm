translate = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())
result = ''
while True:
    a, b = divmod(N, B)
    N = a
    result = translate[b] + result
    if a == 0:
        break
print(result)   