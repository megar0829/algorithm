a = 'AAAA'
b = 'BB'
board = input()
poly = []
sum_board = ''
for i in range(len(board)):
    if board[i] == '.':
        if sum_board != '':
            poly.append(sum_board)
        sum_board = ''
        poly.append(board[i])
    else:
        sum_board += board[i]
if sum_board != '':
    poly.append(sum_board)
result = 0
for i in range(len(poly)):
    if poly[i] != '.':
        n = len(poly[i])
        n_4 = n % 4
        if n % 4 == 0 or n % 2 == 0:
            poly[i] = a * (n // 4) + b * (n_4 // 2)
        else:
            result = -1
            break
if result == -1:
    print(-1)
else:
    print(*poly, sep='')