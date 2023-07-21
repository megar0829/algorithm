import sys
input = sys.stdin.readline

while True:
    triangle = sorted(list(map(int, input().split())))
    if sum(triangle) == 0:
        break
    cnt_triangle = []
    if triangle[2] >= triangle[0] + triangle[1]:
        print('Invalid')
    else:
        for i in triangle:
            cnt_triangle.append(triangle.count(i))
        cnt_triangle.sort(reverse=True)
        if cnt_triangle[0] == 3:
            print('Equilateral')
        elif cnt_triangle[0] == 2:
            print('Isosceles')
        else:
            print('Scalene')
