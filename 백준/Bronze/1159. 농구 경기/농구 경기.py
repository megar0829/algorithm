N = int(input())
first_name = [input() for _ in range(N)]
dict_name = {}
for i in first_name:
    if i[0] not in dict_name:
        dict_name[i[0]] = 1
    else:
        dict_name[i[0]] += 1
result = []
for k, v in dict_name.items():
    if v >= 5:
        result.append(k)
if len(result) == 0:
    print('PREDAJA')
else:
    print(*sorted(result), sep='')