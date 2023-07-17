from datetime import datetime 
n = int(input())
members = {}
members_age = []
for _ in range(n):
    name, day, month, year = list(input().split())
    age = (datetime.today().year - int(year) + 1) \
        + (datetime.today().month - int(month))/10 \
        + (datetime.today().day - int(day))/100
    members[name] = age
    members_age.append(age)
members_age = sorted(members_age)
for k, v in members.items():
    if v == members_age[0]:
        young = k
    elif v == members_age[n-1]:
        old = k
print(young)
print(old)