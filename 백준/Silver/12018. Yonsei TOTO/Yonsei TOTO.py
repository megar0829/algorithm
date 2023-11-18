import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cnt = 0

points = []

for _ in range(n):
    p, l = map(int, input().split())
    point = sorted(list(map(int, input().split())), reverse=True)
    
    if p < l:
        if m:
            m -= 1
            cnt += 1
    
    else:
        points.append(point[l - 1])

if m:
    points.sort()

    for point in points:
        if m <= 0:
            break
        
        if point > m:
            break
        
        else:
            m -= point
            cnt += 1

print(cnt)