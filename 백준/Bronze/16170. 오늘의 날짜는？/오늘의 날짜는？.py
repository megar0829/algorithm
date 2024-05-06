import datetime

time = datetime.datetime.now()

print(time.year)

if time.month < 10:
    print(f'0{time.month}')
else:
    print(time.month)
    
if time.day < 10:
    print(f'0{time.day}')
else:
    print(time.day)