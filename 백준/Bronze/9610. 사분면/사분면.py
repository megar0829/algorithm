N = int(input())
xy_dict = { 
    'Q1' : 0,
    'Q2' : 0,
    'Q3' : 0,
    'Q4' : 0,
    'AXIS' : 0, 
}
for _ in range(N):
    x,y = map(int, input().split())
    if x == 0 or y == 0 or (x == 0 and y == 0):
        xy_dict['AXIS'] += 1
    elif x > 0 and y > 0:
        xy_dict['Q1'] += 1
    elif x < 0 and y > 0:
        xy_dict['Q2'] += 1
    elif x < 0 and y < 0:
        xy_dict['Q3'] += 1
    elif x > 0 and y < 0:
        xy_dict['Q4'] += 1
for k, v in xy_dict.items():
    print(f'{k}: {v}')