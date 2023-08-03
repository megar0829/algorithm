ax, ay, az = list(map(int, input().split()))
cx, cy, cz = list(map(int, input().split()))
bx = cx - az
by = cy // ay
bz = cz - ax
print(bx, by, bz)