T = int(input())
for _ in range(T):
    H, W, N = list(map(int, input().split()))
    rooms = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W): 
            if j+1 < 10:
                rooms[i][j] = str(i+1) + '0' + str(j+1)
            else:
                rooms[i][j] = str(i+1) + str(j+1)
    N_rooms = []
    for i in range(W):
        for j in range(H):
            N_rooms.append(rooms[j][i])
    print(N_rooms[N-1])