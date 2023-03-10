Alp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alp = list('abcdefghijklmnopqrstuvwxyz')
text = input()
result = ''
for i in text:
    if i in Alp:
        ind = Alp.index(i) + 13
        if ind > 25:
            ind -= 26
        result += Alp[ind]
    elif i in alp:
        ind = alp.index(i) + 13
        if ind > 25:
            ind -= 26
        result += alp[ind]
    else:
        result += i
print(result)