T = int(input())
for t in range(1, T + 1):
    answer = 1
    matrix = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if matrix[i][j] in g:
                g.pop(g.index(matrix[i][j]))
            if matrix[j][i] in s:
                s.pop(s.index(matrix[j][i]))
        if len(g) == 0 and len(s) == 0:
            pass
        else:
            answer = 0
            break
    for a in range(0, 8, 3):
        for b in range(0, 8, 3):
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9]   
            for i in range(a, a+3):
                for j in range(b, b+3):
                    if matrix[i][j] in x:
                        x.pop(x.index(matrix[i][j]))
            if len(x) != 0:
                answer = 0
                break
    print(f'#{t} {answer}')