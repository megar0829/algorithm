cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alp = input()
cnt = 0
for i in cro_alp:
    if i in alp:
        cnt += 1
        alp = alp.replace(i, '0')
print(len(alp))