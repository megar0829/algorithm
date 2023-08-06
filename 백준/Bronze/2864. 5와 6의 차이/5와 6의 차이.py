A, B = input().split()
max_a, max_b = '', ''
min_a, min_b = '', ''
for i in A:
    if i == '6':
        max_a += '6'
        min_a += '5'
    elif i == '5':
        max_a += '6'
        min_a += '5'
    else:
        max_a += i
        min_a += i

for i in B:
    if i == '6':
        max_b += '6'
        min_b += '5'
    elif i == '5':
        max_b += '6'
        min_b += '5'
    else:
        max_b += i
        min_b += i

print((int(min_a) + int(min_b)), (int(max_a) + int(max_b)))