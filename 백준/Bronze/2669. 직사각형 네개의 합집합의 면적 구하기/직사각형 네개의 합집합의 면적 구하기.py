matrix = [list(map(int,input().split())) for _ in range(4)]
xy = []
for i in range(4):
    x = list(range(matrix[i][0],matrix[i][2]))
    y = list(range(matrix[i][1],matrix[i][3]))
    for j in x:
        for k in y:
            xy.append((j,k))
xy = set(xy)
print(len(xy))