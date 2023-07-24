import sys
input = sys.stdin.readline

N = int(input())
people = {}
for _ in range(N):
    age, name = input().split()
    if int(age) not in people:
        people[int(age)] = [name]
    else:
        people[int(age)].append(name)
people_age = sorted(people.keys())
for age in people_age:
    if len(people[age]) == 1:
        print(age, *people[age])
    else:
        for name in people[age]:
            print(age, name)