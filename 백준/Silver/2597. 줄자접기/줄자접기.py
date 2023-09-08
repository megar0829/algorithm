def swap(a, b):
    return b, a

N = int(input())
points = []

for i in range(3):
    x, y = sorted(list(map(int, input().split())))
    points.append((x, y))

for i in range(3):
    if points[i][0] == points[i][1]:
        continue
    mid = (points[i][1] + points[i][0]) / 2.0
    
    if mid < N - mid:
        for j in range(i + 1, 3):
            if points[j][0] < mid:
                points[j] = (mid - points[j][0], points[j][1])
            else:
                points[j] = (points[j][0] - mid, points[j][1])

            if points[j][1] < mid:
                points[j] = (points[j][0], mid - points[j][1])
            else:
                points[j] = (points[j][0], points[j][1] - mid)

            if points[j][0] > points[j][1]:
                points[j] = swap(points[j][0], points[j][1])
        
        N = N - mid
    else:
        for j in range(i + 1, 3):
            if mid < points[j][0]:
                points[j] = (mid - (points[j][0] - mid), points[j][1])
            if mid < points[j][1]:
                points[j] = (points[j][0], mid - (points[j][1] - mid))

            if points[j][0] > points[j][1]:
                points[j] = swap(points[j][0], points[j][1])
        
        N = mid

print("{:.1f}".format(N))