massage = input()
h = 0
s = 0
cnt = 0
for i in massage:
    if i == ':':
        cnt += 1
    if i == '-':
        if cnt == 1:
            cnt += 1
    if i == ')':
        if cnt == 2:
            h += 1
            cnt = 0
    if i == '(':
        if cnt == 2:
            s += 1
            cnt = 0        
if h != s:
    if h > s:
        print('happy')
    elif s > h:
        print('sad')
else:
    if s == 0 and h == 0:
        print('none')
    else:
        print('unsure')