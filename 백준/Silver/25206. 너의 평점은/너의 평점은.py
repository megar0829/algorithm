grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F' : 0,
}
unit = 0
cnt_grades = 0
for _ in range(20):
    a, b, c = list(map(str, input().split()))
    if c == 'P':
        pass
    else:
        unit += float(b) * grade[c]
        cnt_grades += float(b)
if cnt_grades == 0:
    print('0.000000')
else:
    print(round(unit / cnt_grades, 6))