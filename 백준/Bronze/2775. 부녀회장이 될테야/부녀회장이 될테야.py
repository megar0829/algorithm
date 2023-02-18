import sys
T = int(sys.stdin.readline())
floor_1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for _ in range(k):
        floor_1.append([0]*14)
    for i in range(k):
        for j in range(14):
            sum_floor = 0
            for l in range(j+1):
                sum_floor += floor_1[i][l]
            floor_1[i+1][j] = sum_floor
    print(floor_1[k][n-1])