ab = input()
a = ''
b = ''
if len(ab) == 2:
    a += ab[0]
    b += ab[1]
elif len(ab) == 3:
    if ab.index('0') == 1:
        a += ab[0:2]
        b += ab[2]
    else:
        a += ab[0]
        b += ab[1:3]
elif len(ab) == 4:
    a += ab[0:2]
    b += ab[2:4]
print(int(a) + int(b))