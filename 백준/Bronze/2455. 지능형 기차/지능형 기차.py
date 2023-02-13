people = []
save = 0
for _ in range(4):
    Out, In = map(int, input().split())
    save = save - Out + In
    people.append(save)
print(max(people))