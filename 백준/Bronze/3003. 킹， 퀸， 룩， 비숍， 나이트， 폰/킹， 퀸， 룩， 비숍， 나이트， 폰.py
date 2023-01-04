x = list(map(int, input().split()))
chess_list = [1, 1, 2, 2, 2, 8]
cnt = 0
m = 0
for n in x:
    chess = chess_list[cnt] - n
    cnt += 1
    print(chess, end=' ')