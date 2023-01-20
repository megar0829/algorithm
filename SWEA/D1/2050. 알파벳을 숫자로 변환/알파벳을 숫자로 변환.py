alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp_dict = {}
for i in alp:
    alp_dict[i] = alp.index(i) + 1
text = input()
for i in text:
    print(alp_dict[i], end=' ')