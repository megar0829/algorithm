t = [int(input()) for _ in range(10)]
ewsn = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}
now = 0
for i in t:
    if i == 1:
        now += 90
    elif i == 2:
        now += 180
    elif i == 3:
        now += 270
    if now >= 360:
        now -= 360
print(ewsn[now])