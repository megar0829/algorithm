A = [list(map(int, input().split())) for _ in range(9)]
max_save = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if A[i][j] >= max_save:
            max_save = A[i][j]
            x, y = i+1 , j+1
print(max_save)
print(x, y)