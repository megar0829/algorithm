long_name = list(input().split('-'))
short_name = ''
for i in long_name:
    short_name += i[0]
print(short_name)
