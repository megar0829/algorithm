import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []
for _ in range(p):
    l, n = input().strip('\n').split()
    l = int(l)
    if not rooms:
        rooms.append([l, [[l, n]]])
    else:
        flag = True
        for i in range(len(rooms)):
            if (rooms[i][0] - 10 <= l <= rooms[i][0] + 10) and len(rooms[i][1]) < m:
                rooms[i][1].append([l, n])
                flag = False
                break
        if flag:
            rooms.append([l, [[l, n]]])
                
for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
        print('Started!')
    else:
        print('Waiting!')
        
    for level, name in sorted(rooms[i][1], key=lambda x:x[1]):
        print(level, name)