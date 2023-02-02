N = int(input())
r_load = list(map(int, input().split()))
save = r_load[0]
h_save = 0
height = []
for i in r_load:
    if i > save:
        h_save += i - save
    else:
        h_save = 0
    save = i
    height.append(h_save)
print(max(height))