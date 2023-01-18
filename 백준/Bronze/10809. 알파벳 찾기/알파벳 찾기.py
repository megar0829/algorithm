alp = 'abcdefghijklmnopqrstuvwxyz'
S = input()
alp_lst = []
for i in alp:
    alp_lst.append(S.find(i))
print(*alp_lst)