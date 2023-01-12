# 연월일 달력
T = int(input())
for t in range(1, T+1):
    days = int(input())
    for i in range(3):
        new_days = []
        if i == 0:
            year = days // 10000
            days = days % 10000
        elif i == 1:
            month = days // 100
            days = days % 100
        else:
            day = days
  
    if (month > 12) or (month <= 0):
        print(f'#{t} {-1}')
        continue
    elif month == 2:
        if day > 28 or day < 0:
            print(f'#{t} {-1}')
            continue
        else:
            if year < 1000:
                new_days.append('0'+str(year))
            else:
                new_days.append(str(year))
            if month < 10:
                new_days.append('0'+str(month))
            else:
                new_days.append(str(month))
            if day < 10:
                new_days.append('0'+str(day))
            else:
                new_days.append(str(day))
    elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if day > 31 or day < 0:
            print(f'#{t} {-1}')
            continue
        else:
            if year < 1000:
                new_days.append('0'+str(year))
            else:
                new_days.append(str(year))
            if month < 10:
                new_days.append('0'+str(month))
            else:
                new_days.append(str(month))
            if day < 10:
                new_days.append('0'+str(day))
            else:
                new_days.append(str(day))
    elif month == 4 or 6 or 9 or 11:
        if day > 30 or day < 0:
            print(f'#{t} {-1}')
            continue
        else:
            if year < 1000:
                new_days.append('0'+str(year))
            else:
                new_days.append(str(year))
            if month < 10:
                new_days.append('0'+str(month))
            else:
                new_days.append(str(month))
            if day < 10:
                new_days.append('0'+str(day))
            else:
                new_days.append(str(day))
    
    print(f'#{t} {new_days[0]}/{new_days[1]}/{new_days[2]}')