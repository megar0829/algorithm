for _ in range(4):
    x1, y1, x2, y2, i1, j1, i2, j2 = list(map(int, input().split()))
    if x2 < i1 or x1 > i2 or y1 > j2 or y2 < j1:
        print('d')
    elif ((x1, y1) == (i2, j2)) or ((x2, y2) == (i1, j1)) or ((x1, y2) == (i2,j1)) or ((x2, y1) == (i1, j2)):
        print('c')
    elif (x1 == i2) or (x2 == i1) or (y1 == j2) or (y2 == j1):
        print('b')
    else:
        print('a')