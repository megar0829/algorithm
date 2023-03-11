month = [30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int,input().split())
if x == 1:
    print(day[(y % 7) - 1])
else:
    for i in range(x - 1):
        y += month[i]
    print(day[(y % 7)])