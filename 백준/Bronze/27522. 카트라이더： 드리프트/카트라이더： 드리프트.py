racer = {}
for _ in range(8):
    time, RB = map(str, input().split())
    racer[time] = RB
ranking = sorted(racer.keys(), reverse=True)
red = 0
blue = 0
for k, v in racer.items():
    if ranking.index(k) == 6:
        if v == 'R':
            red += 8
        else:
            blue += 8
    elif ranking.index(k) == 7:
        if v == 'R':
            red += 10
        else:
            blue += 10
    else:
        if v == 'R':
            red += ranking.index(k) + 1
        else:
            blue += ranking.index(k) + 1
if red > blue:
    print('Red')
else:
    print('Blue')