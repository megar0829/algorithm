code = list(map(int, input().split()))
if code == list(range(1, 9)):
    print('ascending')
elif code == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')