hour_now, minute_now, second_now = input().split(':')
hour_start, minute_start, second_start = input().split(':')
if int(hour_now) < int(hour_start):
    hour = int(hour_start) - int(hour_now)
    minute = int(minute_start) - int(minute_now)
    second = int(second_start) - int(second_now)
    if second < 0:
        second += 60
        minute -= 1
    if minute < 0:
        minute += 60
        hour -= 1
else:
    hour = 24 - (int(hour_now) - int(hour_start))
    minute = 0 - (int(minute_now) - int(minute_start))
    second = 0 - (int(second_now) - int(second_start))
    if second < 0:
        second += 60
        minute -= 1
    if minute < 0:
        minute += 60
        hour -= 1
if hour == 24:
    hour = 0
hour = str(hour)
minute = str(minute)
second = str(second)
if int(hour) < 10:
    hour = '0' + hour
if int(minute) < 10:
    minute = '0' + minute
if int(second) < 10:
    second = '0' + second
print(hour + ':' + minute + ':' + second)