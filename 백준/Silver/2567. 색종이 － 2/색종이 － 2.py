n = int(input())
matrix = [[0]*102 for _ in range(102)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            matrix[i][j] = 1
around = 0
for i in range(101):
    for j in range(101):
        if matrix[i][j] != matrix[i][j+1]:
            around += 1
            
        if matrix[j][i] != matrix[j+1][i]:
            around += 1
print(around)