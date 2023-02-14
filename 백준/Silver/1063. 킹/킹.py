king, stone, N = list(map(str, input().split()))
move = [input() for _ in range(int(N))]

delta = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}
k = (8 - int(king[1]), ord(king[0])-65)
s = (8 - int(stone[1]), ord(stone[0])-65)

for i in move:
    save_k = (k[0] + delta[i][0], k[1] + delta[i][1])
    save_s = (s[0] + delta[i][0], s[1] + delta[i][1])
    if save_k[0] > 7 or save_k[0] < 0 or save_k[1] > 7 or save_k[1] < 0:
        pass
    elif save_k == s and (save_s[0] > 7 or save_s[0] < 0 or save_s[1] > 7 or save_s[1] < 0):
        pass
    else:
        k = save_k
        if k == s:
            s = save_s
k = chr(k[1] + 65) + str(8 - k[0])
s = chr(s[1] + 65) + str(8 - s[0])
print(k)
print(s)