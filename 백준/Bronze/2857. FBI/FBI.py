FBI = [input() for _ in range(5)]
arr = []
for i in range(1, 6):
    if 'FBI' in FBI[i - 1]:
        arr.append(i)

if arr:
    print(*arr)
else:
    print('HE GOT AWAY!')