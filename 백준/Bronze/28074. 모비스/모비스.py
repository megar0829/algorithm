alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp_dict = {}
for n in alp:
    alp_dict[n] = 0

word = list(input())
for i in word:
    alp_dict[i] += 1

if alp_dict['M'] * alp_dict['O'] * alp_dict['B'] * alp_dict['I'] * alp_dict['S']:
    print('YES')
else:
    print('NO')